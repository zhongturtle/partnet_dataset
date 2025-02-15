import bpy
import os
import sys
from math import *
from mathutils import *

modelpath = sys.argv[6]
pngpath = sys.argv[7]
"""
bpy.ops.import_scene.obj(filepath = modelpath)
bpy.data.scenes['Scene'].render.filepath = pngpath
print('rendering')
bpy.ops.render.render( write_still=True, use_viewport=True)
print('rendered')
sys.exit(0) # exit python and blender
print('exited')
"""


bpy.ops.import_scene.obj(filepath = modelpath)
target = bpy.context.selected_objects[0]
#bpy.data.scenes['Scene'].render.filepath = os.path.join(pngpath,)

cam = bpy.data.objects['Camera']
t_loc_x = target.location.x
t_loc_y = target.location.y
cam_loc_x = cam.location.x
cam_loc_y = cam.location.y

#dist = sqrt((t_loc_x-cam_loc_x)**2+(t_loc_y-cam_loc_y)**2)
dist = (target.location.xy-cam.location.xy).length
#ugly fix to get the initial angle right
init_angle  = (1-2*bool((cam_loc_y-t_loc_y)<0))*acos((cam_loc_x-t_loc_x)/dist)-2*pi*bool((cam_loc_y-t_loc_y)<0)

num_steps = 36

for x in range(num_steps):
    alpha = init_angle + (x+1)*2*pi/num_steps
    cam.rotation_euler[2] = pi/2+alpha
    cam.location.x = t_loc_x+cos(alpha)*dist
    cam.location.y = t_loc_y+sin(alpha)*dist
    #file = os.path.join(pngpath, str(x))
    pngpath = pngpath.replace('.png','')
    file = pngpath + str(x) + '.png'
    bpy.context.scene.render.filepath = file
    bpy.ops.render.render( write_still=True ) 



#print('rendering')
#bpy.ops.render.render( write_still=True)
#print('rendered')
sys.exit(0) # exit python and blender
print('exited')
