"""Build and audit a reusable GEOMETRY STUDY, not final painted game art.

blender -b --factory-startup --python-exit-code 1 --python THIS --
  --config house.json --out /absolute/path [--audit-only]
Fault injection (QA): --fault floating-roof|floating-post|missing-roof|clipped
"""
import argparse
import collections
import hashlib
import json
import math
from pathlib import Path
import sys

import bpy
import bmesh
from mathutils import Vector
from mathutils.bvhtree import BVHTree
from bpy_extras.object_utils import world_to_camera_view


def material(name, color):
    mat = bpy.data.materials.new(name)
    mat.diffuse_color = (*color, 1)
    mat.use_nodes = True
    mat.node_tree.nodes.get('Principled BSDF').inputs['Base Color'].default_value = (*color, 1)
    mat.node_tree.nodes.get('Principled BSDF').inputs['Roughness'].default_value = .85
    return mat


def mesh(name, vertices, faces, mat, root):
    data = bpy.data.meshes.new(name)
    data.from_pydata(vertices, [], faces)
    data.update()
    # Consistent outward normals on each closed component.
    bm = bmesh.new()
    bm.from_mesh(data)
    bmesh.ops.recalc_face_normals(bm, faces=bm.faces)
    bm.to_mesh(data)
    bm.free()
    obj = bpy.data.objects.new(name, data)
    bpy.context.collection.objects.link(obj)
    obj.parent = root
    obj.data.materials.append(mat)
    return obj


def box(name, low, high, mat, root):
    x, y, z = low
    X, Y, Z = high
    assert X > x and Y > y and Z > z, name
    return mesh(name, [(x,y,z),(X,y,z),(X,Y,z),(x,Y,z),(x,y,Z),(X,y,Z),(X,Y,Z),(x,Y,Z)],
                [(0,3,2,1),(4,5,6,7),(0,1,5,4),(1,2,6,5),(2,3,7,6),(3,0,4,7)], mat, root)


def slab(name, top, thickness, mat, root):
    return mesh(name, top+[(x,y,z-thickness) for x,y,z in top],
                [(0,1,2,3),(7,6,5,4),(0,4,5,1),(1,5,6,2),(2,6,7,3),(3,7,4,0)], mat, root)


def build(c, root):
    L, D, H, R, O, T = (c[k] for k in ('length','depth','wall_height','ridge_height','overhang','roof_thickness'))
    if not (L > 0 and D > 0 and R > H > .5 and O > 0 and 0 < T < .3):
        raise ValueError('Require positive dimensions, ridge > wall > .5 and 0 < roof thickness < .3')
    wall = material('ivory plaster', (.73,.67,.50))
    roof = material('terracotta', (.48,.12,.055))
    wood = material('oak frame', (.16,.075,.028))
    stone = material('foundation stone', (.34,.38,.40))
    glass = material('blue window', (.06,.22,.28))
    box('foundation', (-L/2-.12,-D/2-.12,0),(L/2+.12,D/2+.12,.25), stone,root)
    profile = [(-D/2,.25),(D/2,.25),(D/2,H),(0,R),(-D/2,H)]
    verts = [(x,y,z) for x in (-L/2,L/2) for y,z in profile]
    faces = [(4,3,2,1,0),(5,6,7,8,9)]+[(i,(i+1)%5,(i+1)%5+5,i+5) for i in range(5)]
    mesh('wall_gables',verts,faces,wall,root)
    slope = (R-H)/(D/2)
    def roof_z(y):
        return R-slope*abs(y)
    for sign, label in ((-1,'far'),(1,'near')):
        y = sign*(D/2+O)
        slab('roof_'+label,[(-L/2-O,0,R+T),(L/2+O,0,R+T),(L/2+O,y,roof_z(y)+T),(-L/2-O,y,roof_z(y)+T)],T,roof,root)
    # Asymmetry makes mirrored/reinvented rotations visible.
    box('door', (L/2,-.53,.25),(L/2+.065,.53,2.18),wood,root)
    for x in (-1.65,.25):
        box('window_frame_'+str(x),(x-.47,D/2,.95),(x+.47,D/2+.07,1.95),wood,root)
        box('window_glass_'+str(x),(x-.36,D/2+.07,1.07),(x+.36,D/2+.085,1.83),glass,root)
    box('rear_window',(-L/2-.05,-.4,1.1),(-L/2,.4,1.9),glass,root)
    cx, cy, half = -1.45, .52, .28
    chimney_bottom = min(roof_z(cy-half),roof_z(cy+half))-.15
    box('chimney',(cx-half,cy-half,chimney_bottom),(cx+half,cy+half,R+.65),stone,root)
    # Open porch: roof rooted at the wall, outer posts reach its underside.
    porch_y, porch_outer, porch_z, porch_drop = D/2-.10, D/2+1.4, 2.55, .5
    slab('porch_roof',[(-.9,porch_y,porch_z),(1.5,porch_y,porch_z),
                       (1.5,porch_outer,porch_z-porch_drop),(-.9,porch_outer,porch_z-porch_drop)],T,roof,root)
    post_y = porch_outer-.15
    post_top = porch_z-porch_drop*(post_y-porch_y)/(porch_outer-porch_y)-T+.025
    for i,x in enumerate((-.7,1.3)):
        box('porch_post_'+str(i),(x-.08,post_y-.08,0),(x+.08,post_y+.08,post_top),wood,root)
    return roof_z


def tree(obj):
    verts = [obj.matrix_world@v.co for v in obj.data.vertices]
    return BVHTree.FromPolygons(verts,[list(p.vertices) for p in obj.data.polygons])


def audit(c, root, camera, scene):
    bpy.context.view_layer.update()
    errors, checks = [], {}
    objs = [o for o in root.children if o.type == 'MESH']
    basis = root.matrix_world.to_3x3()
    gram = basis.transposed() @ basis
    rigid_error = max(abs(gram[i][j] - (1 if i == j else 0)) for i in range(3) for j in range(3))
    checks['rigid_transform_error'] = rigid_error
    checks['rotation_determinant'] = basis.determinant()
    if rigid_error > 1e-5 or abs(basis.determinant()-1) > 1e-5:
        errors.append('assembly: non-rigid deformation or reflection instead of rotation')
    for obj in objs:
        edge_counts = collections.Counter()
        for poly in obj.data.polygons:
            ids = list(poly.vertices)
            edge_counts.update(tuple(sorted((a,b))) for a,b in zip(ids,ids[1:]+ids[:1]))
        if any(n != 2 for n in edge_counts.values()):
            errors.append(obj.name+': open/nonmanifold edges')
        if any(p.area < 1e-10 for p in obj.data.polygons):
            errors.append(obj.name+': degenerate face')
    checks['closed_components'] = len(objs)
    L,D,H,R,T = (c[k] for k in ('length','depth','wall_height','ridge_height','roof_thickness'))
    # At BOTH eaves, test actual mesh against structural support locations.
    for name, sign in (('roof_far',-1),('roof_near',1)):
        obj = bpy.data.objects.get(name)
        if obj is None:
            errors.append(name+': missing')
            continue
        bvh = tree(obj)
        for x in (-L*.4,0,L*.4):
            start = root.matrix_world@Vector((x,sign*D/2,H+1))
            hit, _, _, _ = bvh.ray_cast(start, Vector((0,0,-1)), 2)
            if hit is None or abs((hit.z-T)-H) > .025:
                errors.append(name+': eave does not meet wall at x='+str(x))
    checks['eave_ray_probes'] = 6
    for name in ('porch_post_0','porch_post_1'):
        obj = bpy.data.objects[name]
        points = [obj.matrix_world@v.co for v in obj.data.vertices]
        if abs(min(v.z for v in points)) > .005:
            errors.append(name+': not grounded')
        center = sum(points,Vector())/len(points)
        top = max(v.z for v in points)
        hit, _, _, _ = tree(bpy.data.objects['porch_roof']).ray_cast(Vector((center.x,center.y,top+1)),Vector((0,0,-1)),2)
        if hit is None or abs((hit.z-T)-top) > .04:
            errors.append(name+': roof contact gap')
    checks['post_contacts'] = 2
    # Chimney must penetrate the roof, with an exposed upper end.
    chimney = bpy.data.objects['chimney']
    pts = [chimney.matrix_world@v.co for v in chimney.data.vertices]
    center = sum(pts,Vector())/len(pts)
    roof = bpy.data.objects.get('roof_near')
    hit = tree(roof).ray_cast(Vector((center.x,center.y,R+2)),Vector((0,0,-1)),R+3)[0] if roof else None
    if hit is None or not min(v.z for v in pts) < hit.z < max(v.z for v in pts):
        errors.append('chimney: does not intersect its roof')
    # No auto-framing each view: fixed camera, fixed scale, common world pivot.
    for obj in objs:
        for vertex in obj.data.vertices:
            p = world_to_camera_view(scene,camera,obj.matrix_world@vertex.co)
            if p.z <= 0 or not (.03 <= p.x <= .97 and .03 <= p.y <= .97):
                errors.append(obj.name+': frame margin below 3%')
                break
    checks['framing_margin'] = .03
    return {'status':'fail' if errors else 'pass','checks':checks,'errors':errors}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--config',required=True)
    parser.add_argument('--out',required=True)
    parser.add_argument('--audit-only',action='store_true')
    parser.add_argument('--fault',choices=['floating-roof','floating-post','missing-roof','clipped','squashed','swapped-annex'])
    args = parser.parse_args(sys.argv[sys.argv.index('--')+1:])
    c = json.loads(Path(args.config).read_text())
    out = Path(args.out).resolve()
    out.mkdir(parents=True,exist_ok=True)
    bpy.ops.wm.read_factory_settings(use_empty=True)
    scene = bpy.context.scene
    root = bpy.data.objects.new('building_world_pivot',None)
    bpy.context.collection.objects.link(root)
    build(c,root)
    bpy.context.view_layer.update()
    # Freeze the designed assembly BEFORE faults or yaw changes. Later checks
    # compare geometry AND child transforms, not only mesh coordinates.
    def assembly_signature():
        return hashlib.sha256(repr(sorted((o.name,[tuple(v.co) for v in o.data.vertices],
            [tuple(row) for row in o.matrix_basis]) for o in root.children)).encode()).hexdigest()
    designed_signature = assembly_signature()
    if args.fault == 'floating-roof':
        bpy.data.objects['roof_near'].location.z += .45
    elif args.fault == 'floating-post':
        bpy.data.objects['porch_post_0'].location.z += .3
    elif args.fault == 'missing-roof':
        bpy.data.objects.remove(bpy.data.objects['roof_far'],do_unlink=True)
    elif args.fault == 'squashed':
        root.scale.y = .55
    elif args.fault == 'swapped-annex':
        bpy.data.objects['porch_roof'].location.y -= 3
    data = bpy.data.cameras.new('locked_camera')
    camera = bpy.data.objects.new('locked_camera',data)
    bpy.context.collection.objects.link(camera)
    scene.camera = camera
    data.type = 'ORTHO'
    data.ortho_scale = 3 if args.fault == 'clipped' else c['ortho_scale']
    a,e = map(math.radians,(c['azimuth'],c['elevation']))
    target = Vector((0,0,2.2))
    camera.location = target+20*Vector((math.cos(a)*math.cos(e),math.sin(a)*math.cos(e),math.sin(e)))
    camera.rotation_euler = (target-camera.location).to_track_quat('-Z','Y').to_euler()
    engine_ids = [item.identifier for item in scene.render.bl_rna.properties['engine'].enum_items]
    scene.render.engine = 'CYCLES' if 'CYCLES' in engine_ids else 'BLENDER_EEVEE'
    if scene.render.engine == 'CYCLES':
        scene.cycles.samples = 16
        scene.cycles.use_denoising = True
    scene.render.resolution_x = scene.render.resolution_y = c['resolution']
    scene.render.resolution_percentage = 100
    scene.render.film_transparent = True
    scene.render.image_settings.file_format = 'PNG'
    scene.render.image_settings.color_mode = 'RGBA'
    scene.world = bpy.data.worlds.new('studio')
    scene.world.use_nodes = True
    scene.world.node_tree.nodes['Background'].inputs['Color'].default_value = (.5,.5,.5,1)
    scene.world.node_tree.nodes['Background'].inputs['Strength'].default_value = .7
    lightdata = bpy.data.lights.new('key','AREA')
    light = bpy.data.objects.new('key',lightdata)
    bpy.context.collection.objects.link(light)
    light.location = (2,-4,10)
    light.rotation_euler = (Vector((0,0,2))-light.location).to_track_quat('-Z','Y').to_euler()
    lightdata.energy, lightdata.shape, lightdata.size = 1400,'DISK',7
    scene.view_settings.view_transform = 'Standard'
    report = {'blender':bpy.app.version_string,'engine':scene.render.engine,'fault':args.fault,
              'scope':'Parametric gable study; no full mesh self-intersection/structural engineering certification',
              'config':c,'views':[]}
    # Compare local-geometry hash and camera state before/after root rotations.
    signature = lambda: hashlib.sha256(repr([(o.name,[tuple(v.co) for v in o.data.vertices]) for o in root.children]).encode()).hexdigest()
    original = signature()
    for yaw in c['yaws']:
        root.rotation_euler.z = math.radians(yaw)
        bpy.context.view_layer.update()
        result = audit(c,root,camera,scene)
        result['assembly_signature_matches_design'] = assembly_signature() == designed_signature
        if not result['assembly_signature_matches_design']:
            result['errors'].append('assembly: parts changed relative to the designed building')
            result['status'] = 'fail'
        if signature() != original:
            result['errors'].append('local geometry changed during rotation')
            result['status'] = 'fail'
        result.update(yaw=yaw,mesh_sha256=signature())
        # Cross-check Blender's actual projection against independent formula.
        px = world_to_camera_view(scene,camera,Vector((1,0,2.2)))
        px0 = world_to_camera_view(scene,camera,Vector((0,0,2.2)))
        expected = (-math.sin(a)/data.ortho_scale,-math.sin(e)*math.cos(a)/data.ortho_scale)
        error = max(abs((px.x-px0.x)-expected[0]),abs((px.y-px0.y)-expected[1]))
        result['projection_max_error_normalized'] = error
        if error > 1e-6:
            result['errors'].append('Blender projection disagrees with analytic basis')
            result['status'] = 'fail'
        if result['status'] == 'pass' and not args.audit_only:
            scene.render.filepath = str(out/f'yaw-{yaw:g}.png')
            bpy.ops.render.render(write_still=True)
            result['render'] = scene.render.filepath
            # Verify exported pixels, rather than trusting render completion.
            import numpy as np
            img = bpy.data.images.load(scene.render.filepath,check_existing=False)
            pixels = np.empty(len(img.pixels),dtype=np.float32)
            img.pixels.foreach_get(pixels)
            alpha = pixels.reshape(img.size[1],img.size[0],4)[:,:,3]
            rows,cols = np.where(alpha > .01)
            result['visible_pixels'] = int(len(rows))
            result['transparent_pixels'] = int(np.count_nonzero(alpha < .01))
            if len(rows):
                result['alpha_bbox_bottom_origin'] = [int(cols.min()),int(rows.min()),int(cols.max()+1),int(rows.max()+1)]
                if min(cols.min(),rows.min(),img.size[0]-1-cols.max(),img.size[1]-1-rows.max()) < 2:
                    result['errors'].append('exported pixels touch canvas border')
                    result['status'] = 'fail'
            if not len(rows) or not result['transparent_pixels']:
                result['errors'].append('blank render or missing transparency')
                result['status'] = 'fail'
            bpy.data.images.remove(img)
            if yaw == 0:
                # Visible structural edge coordinates from Blender itself, for
                # an end-to-end check with the independent camera fitter.
                L,D,H = (c[k] for k in ('length','depth','wall_height'))
                def pixel(p):
                    q = world_to_camera_view(scene,camera,Vector(p))
                    return [q.x*c['resolution'],(1-q.y)*c['resolution']]
                edge_sets = {
                    'x_edges': [[(-L/2,D/2,z),(L/2,D/2,z)] for z in (.25,H)],
                    'y_edges': [[(L/2,-D/2,z),(L/2,D/2,z)] for z in (.25,H)],
                    'z_edges': [[(L/2,y,.25),(L/2,y,H)] for y in (-D/2,D/2)]}
                annotations = {k:[[pixel(p) for p in line] for line in lines] for k,lines in edge_sets.items()}
                annotations['provenance'] = 'Synthetic Blender mesh edges, not measurements of accepted artwork'
                (out/'camera-edges.json').write_text(json.dumps(annotations,indent=2))
        report['views'].append(result)
    report['status'] = 'fail' if any(v['status']=='fail' for v in report['views']) else 'pass'
    (out/'report.json').write_text(json.dumps(report,indent=2))
    if report['status'] == 'pass' and not args.audit_only:
        root.rotation_euler.z = math.radians(c['yaws'][0])
        bpy.ops.wm.save_as_mainfile(filepath=str(out/'geometry-study.blend'))
    print('SPATIAL_QA',json.dumps(report))
    if report['status'] == 'fail':
        raise RuntimeError('Spatial QA failed; see report.json')


if __name__ == '__main__':
    main()
