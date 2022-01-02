
bl_info = {
    "name": "Human Primitive Lite",
    "author": "BlenderBoi",
    "version": (1, 0),
    "blender": (3, 00, 0),
    "description": "",
    "warning": "",
    "location": "View3D > Add > Mesh",
    "wiki_url": "",
    "category": "Add Mesh",
}

import bpy
from . import AddMenu


from . import HP_BodyPart_Add_Male_Base
from . import HP_BodyPart_Add_Female_Base

modules = [HP_BodyPart_Add_Male_Base, HP_BodyPart_Add_Female_Base, AddMenu]

def register():

    for module in modules:
        module.register()

def unregister():

    for module in modules:
        module.unregister()

if __name__ == "__main__":
    register()
