bl_info = {
    "name": "Blend2Mesh",
    "author": "Ahmed Salih",
    "version": (1, 0),
    "blender": (2, 80, 0),
    "location": "View3D > Add > Mesh > New Object",
    "description": "Blend2Mesh - export mesh to binary format",
    "warning": "",
    "wiki_url": "",
    "category": "Add Mesh",
}

import os
import bpy
import numpy as np

from bpy.types import (
    AddonPreferences,
    Operator,
    Panel,
    PropertyGroup,
)


from bpy.props import (StringProperty)
    
def GenMesh(self, context):        # execute() is called when running the operator.
    
    #Code to ensure that we are always saving in path of blend file
    # If file has not been saved it will output an error
    filepath = bpy.data.filepath
    directory = os.path.dirname(filepath)
    try:
        os.chdir(directory)
    except:
        self.report({'ERROR'}, "File must be saved first")
        return {'CANCELLED'}
    
    bpy.ops.object.mode_set(mode='OBJECT')
    obj = bpy.context.object
    bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
    mesh = obj.data

    # Number of elements, start from 0
    n = len(mesh.polygons)
    
    invvert = np.zeros(n,dtype=np.int)
    for i in range(0,n):
        vert = mesh.polygons[i].vertices[:]
        invvert[i] = len(vert)
    
    maxvert = np.max(invvert)
    NodesGeneral = np.empty((n,maxvert),dtype=np.float) # n maxvert
    NodesGeneral.fill(np.NaN)
    for i in range(0,n):
        for j in range(0,invvert[i]):
            NodesGeneral[i,j] = mesh.polygons[i].vertices[j]

    nV = len(mesh.vertices)    
    Vertices = np.zeros((nV,3),dtype=np.float)
    for i in range(0,nV):
        for j in range(0,3):
            Vertices[i,j] = mesh.vertices[i].co[j]

    fileName = bpy.context.object.name
    
    np.save(fileName + "Elems", NodesGeneral)
    
    # Saving vertices
    np.save(fileName + "Nodes", Vertices)
    
    
    bpy.ops.object.mode_set(mode='OBJECT')
    
#This function makes small pop-up menu
class OBJECT_OT_blend2mesh(Operator):
    """Function to generate mesh binary files"""      # Use this as a tooltip for menu items and buttons.
    bl_idname = "object.blend2mesh"        # Unique identifier for buttons and menu items to reference.
    bl_label = "Blend2Mesh"         # Display name in the interface.
    bl_options = {'REGISTER', 'UNDO'}  # Enable undo for the operator.
    bl_description = "Generates binary files for reading in external programs"
    bl_space_type  = "VIEW_3D"
    bl_region_type = "UI"
    
    
    #To ensure only mesh can be chosen
    @classmethod
    def poll(cls,context):
        return context.object.select_get() and context.object.type == 'MESH'
    
    def execute(self, context):
    
        GenMesh(self, context)
        self.report({'INFO'}, "Mesh files have been succesfully generated")
        return {'FINISHED'}


def menu_func(self,context):
    self.layout.operator(
    OBJECT_OT_blend2mesh.bl_idname,
    icon='TRIA_UP',
    )
    
    
# Registration

def register():
    bpy.utils.register_class(OBJECT_OT_blend2mesh)
    bpy.types.VIEW3D_MT_object.append(menu_func)

def unregister():
    bpy.utils.unregister_class(OBJECT_OT_blend2mesh)
    bpy.types.VIEW3D_MT_object.remove(menu_func)
    
# This allows you to run the script directly from Blender's Text editor
# to test the add-on without having to install it.
if __name__ == "__main__":
    register()