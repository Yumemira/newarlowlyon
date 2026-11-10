"""Render coarse architectural masses, not finished game art.
--config JSON --out DIR
JSON: {camera_file?: relative JSON path, camera?: {azimuth_deg,elevation_deg,
projection,ortho_scale,lens_mm?,distance?,target,resolution,status}, yaws?: {facade:0,left:-90,right:90,
diagonal:-45}, buildings:[{id, parts:[{shape,size:[x,y,z],at:[x,y,z],
color?:[r,g,b],yaw?:degrees}], art_brief?:string}]}
Shapes: box,gable,hip,vault,ellipsoid,cylinder,cone. Sizes are full bounding
dimensions; at is their bounding-box center. Roof ridges run along local X.
"""
import argparse
import json
import math
from pathlib import Path
import sys
import time

import bpy
from mathutils import Vector
from bpy_extras.object_utils import world_to_camera_view


def form(p, root, i):
    shape = p['shape']
    if shape in ('box', 'ellipsoid', 'cylinder', 'cone'):
        if shape == 'box':
            bpy.ops.mesh.primitive_cube_add(size=2)
        elif shape == 'ellipsoid':
            bpy.ops.mesh.primitive_uv_sphere_add(segments=12, ring_count=8, radius=1)
        elif shape == 'cylinder':
            bpy.ops.mesh.primitive_cylinder_add(vertices=12, radius=1, depth=2)
        else:
            bpy.ops.mesh.primitive_cone_add(vertices=12, radius1=1, radius2=0, depth=2)
        obj = bpy.context.object
    else:
        if shape in ('gable', 'hip'):
            v = [(-1,-1,-1),(1,-1,-1),(1,1,-1),(-1,1,-1)]
            r = 1 if shape == 'gable' else .55
            v += [(-r,0,1),(r,0,1)]
            f = [(3,2,1,0),(0,1,5,4),(2,3,4,5),(3,0,4),(1,2,5)]
        elif shape == 'vault':
            section = [(math.cos(j*math.pi/8), -1+2*math.sin(j*math.pi/8)) for j in range(9)]
            v = [(x,y,z) for x in (-1,1) for y,z in section]
            n = len(section)
            f = [tuple(reversed(range(n))),tuple(range(n,2*n))]
            f += [(j,(j+1)%n,(j+1)%n+n,j+n) for j in range(n)]
        else:
            raise ValueError('Unsupported sketch shape: '+shape)
        mesh = bpy.data.meshes.new(shape)
        mesh.from_pydata(v, [], f)
        mesh.update()
        obj = bpy.data.objects.new(shape, mesh)
        bpy.context.collection.objects.link(obj)
    obj.name = f'{i:02d}_{shape}'
    obj.parent = root
    obj.location = p['at']
    assert len(p['size']) == 3 and min(p['size']) > 0
    obj.scale = [s/2 for s in p['size']]
    obj.rotation_euler.z = math.radians(p.get('yaw', 0))
    obj.color = (*p.get('color', [.55,.6,.64]), 1)
    return obj


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--config', type=Path, required=True)
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args(sys.argv[sys.argv.index('--')+1:])
    config = json.loads(args.config.read_text())
    camera = json.loads((args.config.parent/config['camera_file']).read_text()) if 'camera_file' in config else config['camera']
    yaws = config.get('yaws', {'facade':0, 'left':-90, 'right':90, 'diagonal':-45})
    out = args.out.resolve()
    out.mkdir(parents=True, exist_ok=True)
    start = time.monotonic()
    report = {'camera':camera,'yaws':yaws,'buildings':[], 'limitations':'Coarse image-generation guides. Framing/rigidity only; not detailed contact or art approval.'}
    for building in config['buildings']:
        name = building['id']
        assert name and Path(name).name == name and name not in ('.','..')
        bpy.ops.wm.read_factory_settings(use_empty=True)
        scene = bpy.context.scene
        scene.render.engine = 'BLENDER_WORKBENCH'
        scene.render.resolution_x, scene.render.resolution_y = camera.get('resolution',[384,384])
        scene.render.resolution_percentage = 100
        scene.render.film_transparent = True
        scene.render.image_settings.file_format = 'PNG'
        scene.render.image_settings.color_mode = 'RGBA'
        scene.display.shading.color_type = 'OBJECT'
        scene.display.shading.light = 'STUDIO'
        scene.display.shading.show_shadows = True
        scene.display.shading.show_cavity = False
        scene.view_settings.view_transform = 'Standard'
        root = bpy.data.objects.new('whole_building_pivot', None)
        scene.collection.objects.link(root)
        objects = [form(p,root,i) for i,p in enumerate(building['parts'])]
        assert objects, 'A sketch needs at least one mass'
        local = [o.matrix_basis.copy() for o in objects]
        data = bpy.data.cameras.new('shared_camera')
        data.type = camera.get('projection', 'ORTHO')
        assert data.type in ('ORTHO', 'PERSP'), 'Sketches support ORTHO/PERSP cameras'
        data.ortho_scale = camera['ortho_scale']
        data.sensor_fit = 'HORIZONTAL'
        data.sensor_width = 36
        data.lens = camera.get('lens_mm', 50)
        cam = bpy.data.objects.new('shared_camera',data)
        scene.collection.objects.link(cam)
        a,e = [math.radians(camera[k]) for k in ('azimuth_deg','elevation_deg')]
        target = Vector(camera['target'])
        cam.location = target+camera.get('distance',20)*Vector((math.cos(a)*math.cos(e),math.sin(a)*math.cos(e),math.sin(e)))
        cam.rotation_euler = (target-cam.location).to_track_quat('-Z','Y').to_euler()
        scene.camera = cam
        folder = out/name
        folder.mkdir(exist_ok=True)
        frames = []
        for view,yaw in yaws.items():
            assert Path(view).name == view and view not in ('.','..')
            root.rotation_euler.z = math.radians(yaw)
            bpy.context.view_layer.update()
            coords = [world_to_camera_view(scene,cam,o.matrix_world@Vector(v)) for o in objects for v in o.bound_box]
            fits = all(.02 < p.x < .98 and .02 < p.y < .98 and p.z > 0 for p in coords)
            stable = all(o.matrix_basis == m for o,m in zip(objects,local))
            assert fits and stable, f'{name}/{view}: framing or local transform failed'
            scene.render.filepath = str(folder/(view+'.png'))
            bpy.ops.render.render(write_still=True)
            frames.append({'view':view,'image':f'{name}/{view}.png'})
        root.rotation_euler.z = 0
        bpy.context.view_layer.update()
        bpy.ops.wm.save_as_mainfile(filepath=str(folder/'sketch.blend'))
        report['buildings'].append({'id':name,'masses':len(objects),'frames':frames,'art_brief':building.get('art_brief',''),'passed':True})
    report['seconds'] = round(time.monotonic()-start,3)
    (out/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'buildings':len(report['buildings']),'masses':sum(b['masses'] for b in report['buildings']),'seconds':report['seconds'],'passed':True}))


if __name__ == '__main__':
    main()
