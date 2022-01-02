import bpy
from . import Utility
import os
import bmesh
import mathutils
import math


#Settings
SETTINGS_File_Name = "Female_Human.blend"
SETTINGS_Default_Name = "Female_Human"
SETTINGS_ID_Name = "mesh.human_primitive_lite_basehuman_female"
SETTINGS_Label = "Add Human (Female)"

###########################################################

assets_path = "/Assets/" + SETTINGS_File_Name
assets_Folder = Utility.get_asset_filepath(assets_path)


ENUM_Position = [("CURSOR","Cursor","Cursor"), ("CENTER","Center","Center")]

def load_assets():

    assets_lists =[]

    with bpy.data.libraries.load(str(assets_Folder)) as (data_from, data_to):
        for object in data_from.objects:
            assets_lists.append(object)

    assets_lists = sorted(assets_lists)

    return assets_lists


class HP_LITE_OT_Add_Female_Human(bpy.types.Operator):

    bl_idname = SETTINGS_ID_Name
    bl_label = SETTINGS_Label
    bl_options = {'UNDO', 'REGISTER'}

    name: bpy.props.StringProperty(default=SETTINGS_Default_Name)
    position: bpy.props.EnumProperty(items = ENUM_Position)

    assets_lists = []

    def invoke(self, context, event):

        self.assets_lists = load_assets()
        self.cursor_position = context.scene.cursor.location.copy()

        return self.execute(context)


    def draw(self, context):

        layout = self.layout
        col = layout.column(align=True)

        col.prop(self, "name", text="Name")

        if context.mode == "OBJECT":
            col.prop(self, "position", text="Position")



    def execute(self, context):

        mode = context.mode
        context.view_layer.update()

        if mode == "OBJECT":

            path = str(assets_Folder)
            section = "\\Object\\"
            directory = path + section

            filename = self.assets_lists[0]

            bpy.ops.wm.append(filename=filename, directory=directory)

            Mesh_Object = None
            Armature_Object = None

            Objects = [obj for obj in context.selected_objects]

            for obj in Objects:

                obj.name = self.name
                obj.location = (0, 0, 0)
                Mesh_Object = obj

                obj.select_set(True)
                context.view_layer.objects.active = obj
                bpy.ops.object.convert(target='MESH')

                if self.position == "CURSOR":
                    obj.location = self.cursor_position
                if self.position == "CENTER":
                    obj.location = (0, 0, 0)



        context.view_layer.update()

        return {'FINISHED'}

classes = [HP_LITE_OT_Add_Female_Human]

def register():


    for cls in classes:
        bpy.utils.register_class(cls)



def unregister():

    for cls in classes:
        bpy.utils.unregister_class(cls)

if __name__ == "__main__":
    register()
