import bpy

def draw_primitive_lite(self, context):
    layout = self.layout
    if context.mode == "OBJECT":
        layout.separator()

        operator = layout.operator("mesh.human_primitive_lite_basehuman_male", text="Human (Male)",icon='USER')
        operator = layout.operator("mesh.human_primitive_lite_basehuman_female", text="Human (Female)",icon='USER')

def register():

    bpy.types.VIEW3D_MT_mesh_add.append(draw_primitive_lite)


def unregister():

    bpy.types.VIEW3D_MT_mesh_add.remove(draw_primitive_lite)


if __name__ == "__main__":
    register()
