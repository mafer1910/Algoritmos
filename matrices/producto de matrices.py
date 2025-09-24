# -*- coding: utf-8 -*-
"""
Created on Thu Aug 28 23:39:42 2025

@author: MaFer
"""

matriz1=[[2,6],
         [5,7],
         [1,4]]

matriz2=[[1,2,5],
         [4,5,2]]
mult=[]
for i in range(0,len(matriz1)):
    filas=[]
    suma=0
    for j in range(0,len(matriz1[i])):
        suma+=(matriz1[i][j])*(matriz2[j][i])
    mult.append(suma)
    print(mult[i])