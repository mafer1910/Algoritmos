# -*- coding: utf-8 -*-
"""
Created on Thu Aug 28 23:30:29 2025

@author: MaFer
"""

matriz=[[1,5,7],
        [7,3,8],
        [9,3,6]]
transpuesta=[]
for i in range(0,3):
    fila=[]
    for j in range(0,3):
        fila.append(matriz[j][i])
    transpuesta.append(fila)
    print(transpuesta[i])
    