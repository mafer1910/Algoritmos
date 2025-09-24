# -*- coding: utf-8 -*-
"""
Created on Tue Sep  9 00:00:41 2025

@author: MaFer
"""

def paths(edges,camino,source,dest,exito):
    if camino[len(camino)-1]==dest: 
        return [camino[:]]
    caminos=[]
    for i in range(0,len(edges)):
        if edges[i][0]==camino[len(camino)-1]:
            camino.append(edges[i][1]) 
            caminos.extend(paths(edges, camino, source, dest,exito))
            camino.pop()
    return caminos
        

edges = [[0, 3], [0, 1], [1, 3], [2, 1], [2, 0]]
#[[0, 1], [1, 2], [1, 3], [2, 3]]
camino=[2]
source=2
dest=3
exito=False
print(paths(edges,camino,source,dest,exito))
