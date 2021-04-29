# exports each selected object into its own file

import bpy
import os

basedir = "/Users/jordankehrer/TTS/jk12559/tank-duel-tts/aids/models"

view_layer = bpy.context.view_layer

obj_active = view_layer.objects.active
selection = bpy.context.selected_objects

bpy.ops.object.select_all(action='DESELECT')

for obje in selection:

    obje.select_set(True)

    # some exporters only use the active objectß
    view_layer.objects.active = obje

    name = bpy.path.clean_name(obje.name)
    fn = os.path.join(basedir, name)

    bpy.ops.object.origin_set(type='GEOMETRY_ORIGIN')
    
    current_location = obje.location[:]

    obje.location=[0,0,0]

    bpy.ops.export_scene.obj(filepath=fn + ".obj", use_selection=True)

    obje.location = current_location
    
    bpy.ops.object.origin_set(type='ORIGIN_CURSOR')

    obje.select_set(False)

    print("written:", fn)


view_layer.objects.active = obj_active

for obj in selection:
    obj.select_set(True)
