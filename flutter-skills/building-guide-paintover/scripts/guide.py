"""Render readable geometry cues from an existing Blender scene, without remodeling.
Blender -b --factory-startup scene.blend --python-exit-code 1 --python guide.py --
  --views '{"facade":90,"side":0}' --out /absolute/guide-folder [--root NAME]
Use the saved scene's actual yaw convention. Camera/shape unchanged; neutral
preview appearance, object outlines, and higher raster resolution only.
"""
import argparse
import json
import math
from pathlib import Path
import sys

import bpy


def main():
    p=argparse.ArgumentParser(description=__doc__,formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument('--views',required=True,help='JSON mapping of view names to world yaw degrees')
    p.add_argument('--out',type=Path,required=True)
    p.add_argument('--root',help='Optional explicit assembly root object name')
    a=p.parse_args(sys.argv[sys.argv.index('--')+1:])
    views=json.loads(a.views)
    scene=bpy.context.scene
    root=bpy.data.objects.get(a.root) if a.root else next((bpy.data.objects.get(n) for n in ('whole_building_pivot','BUILDING_rigid_pivot') if bpy.data.objects.get(n)),None)
    if root is None or scene.camera is None:
        raise ValueError('Need a saved camera and named assembly root; pass --root when necessary')
    camera=scene.camera
    camera_matrix=camera.matrix_world.copy()
    projection=camera.data.type
    transforms={o.name:o.matrix_basis.copy() for o in root.children}
    scene.render.engine='BLENDER_WORKBENCH'
    scene.render.resolution_percentage=100
    old=(scene.render.resolution_x,scene.render.resolution_y)
    factor=768/max(old)
    scene.render.resolution_x=max(1,round(old[0]*factor))
    scene.render.resolution_y=max(1,round(old[1]*factor))
    scene.render.film_transparent=True
    scene.render.image_settings.file_format='PNG'
    scene.render.image_settings.color_mode='RGBA'
    shading=scene.display.shading
    shading.light='STUDIO'
    shading.color_type='OBJECT'
    shading.show_object_outline=True
    shading.object_outline_color=(.045,.055,.065)
    shading.show_cavity=False
    shading.show_shadows=True
    for obj in scene.objects:
        if obj.type=='MESH':obj.color=(.62,.66,.70,1)
    a.out.mkdir(parents=True,exist_ok=True)
    for name,yaw in views.items():
        assert Path(name).name==name and name not in ('.','..')
        root.rotation_euler.z=math.radians(yaw)
        bpy.context.view_layer.update()
        assert camera.matrix_world==camera_matrix and camera.data.type==projection
        assert all(o.matrix_basis==transforms[o.name] for o in root.children)
        scene.render.filepath=str((a.out/(name+'.png')).resolve())
        bpy.ops.render.render(write_still=True)
    manifest={'source_blend':bpy.data.filepath,'projection':projection,'views':views,
              'resolution':[scene.render.resolution_x,scene.render.resolution_y],
              'changes':'Neutral preview appearance and contours only; saved source scene is not overwritten.'}
    (a.out/'guides.json').write_text(json.dumps(manifest,indent=2)+'\n')
    print(json.dumps({'views':len(views),'projection':projection,'source_scene_unchanged_on_disk':True}))


if __name__=='__main__':main()
