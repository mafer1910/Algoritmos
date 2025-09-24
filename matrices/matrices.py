# -*- coding: utf-8 -*-
"""
Created on Thu Aug 28 12:19:57 2025

@author: MaFer

"""
import random 

#n=int(random.radint(0,50))
filas=int(input("Ingrese las filas: "))
columnas=int(input("Ingrese las columnas: "))
matriz=[]
matriz2=[]
for i in range(0,filas):
    fila=[]
    a=1
    for j in range(0,columnas):
        fila.append(a)
        a+=1
    matriz.append(fila)
    
for i in range(0,len(matriz)):
    matriz2.append(matriz[i])
    print(matriz2[i],"\n")