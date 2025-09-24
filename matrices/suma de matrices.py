# -*- coding: utf-8 -*-
"""
Created on Thu Aug 28 23:22:51 2025

@author: MaFer
"""

matriz1=[[1,2,3],[4,5,6],[7,8,9]]
matriz2=[[2,4,6],[8,3,7],[6,2,7]]
suma=[]
for i in range(0,len(matriz1)):
    fila=[]
    for j in range(0,len(matriz1[i])):
        fila.append(matriz1[i][j]+matriz2[i][j])
    suma.append(fila)
    print(suma[i])
        

