# Blend2Mesh
Blend2Mesh is a simple add-on written in Python, which allows the user to fast and effectively export different Blender geometries to binary files, which allows for fast reading/loading in external programs. This tool works on any mesh inside of Blender, but will not work for curves etc. It has to be a mesh object. It has been developed for Blender 2.80.

# Installation and Use
Installing this tool is fairly easy. Download "Blend2Mesh" and save it somewhere  on your computer. Then open Blender, in the top left corner, "Edit" -> "Preferences" -> "Add-ons". In this new window which has been opened, press "Install" and locate the downloaded file. After this has been done search for "Blend2Mesh" and tick the check box to make the add-on available for use.

![Link Text](https://github.com/AhmedSalih3d/Blend2Mesh/blob/master/README_pictures/ContinuumElement.png)

Now when working in Blender it is possible, either by clicking the "Object" button and find "Blend2Mesh" option or by pressing F3 and searching for the "Blend2Mesh"
command. Remember, this will only work with meshes so have one selected before hand - also files will be output where the blend file is saved.

# The File Format
If you are familiar with Python, the file format is the single coloumn ".npy" format, which has a header with varius information (in readable format) and then rest of the binary data filled in. Two files will be output. "FileName-Elems.npy" will hold the information regarding which elements consists of which vertices/nodes. "FileName-Nodes.npy" will hold information about the spatial coordinates of each node. Using this information it is possible to replot/use this mesh in some kind of other software, for an example 2D FEM simulations.

# Extra: Matlab Reader

For convenience a function has been developed in Matlab, which showcases a possible way of how to read these files in. The code looks deceptively simply, but is the fastest way Matlab wise to read the data in, according to my tests / current knowledge. To use this function you will need to visit;
https://github.com/kwikteam/npy-matlab and as a minimum download their functions,
"readNPY" and "readNPYheader". When this is done ensure that everything you need to open is on Matlab's path and you will be able to vizualise the mesh you made in Blender, now in Matlab.
As a final note; remember to read licenses to check they suit your application.

# Use in Scientific Papers etc.

If you have used this tool in writing your journal/paper, I would really appreciate if you would reach out to me and/or reference this Github if it makes sense to do so. Thanks in advance.

# Thanks to..

My FEM teacher for taking time to advise me on how to improve this tool and speed up its performance.
