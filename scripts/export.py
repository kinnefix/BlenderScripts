import bpy, bmesh, struct
import numpy as np
obj = bpy.context.active_object

indices=[]
vertices=[]
uv=[]
for face in obj.data.polygons:
    idx = face.vertices[:]
    for index in idx:
        indices.append(index)
for vert in obj.data.vertices:
    vertices.append(vert.co.x)
    vertices.append(vert.co.y)
    vertices.append(vert.co.z)
for loop in obj.data.loops :
    uv_coords = obj.data.uv_layers[0].data[loop.index].uv
    uv.append(uv_coords.x)
    uv.append(uv_coords.y)
data=struct.pack("=III%sI%sd%sd" %(len(indices), len(vertices), len(uv)), len(indices), len(vertices), len(uv), *indices, *vertices, *uv)
open('/data/model.dat', 'wb').write(data)