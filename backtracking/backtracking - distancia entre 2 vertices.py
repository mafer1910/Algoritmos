# -*- coding: utf-8 -*-
"""
Created on Mon Sep  8 00:23:00 2025

@author: MaFer
"""

#camino con cierta distancia de vertice a vertice
#el vector de vectores edgeList[] contiene 3 enteros [u,v,w] representando una arista de u a v con distancia w
#el siguiente codigo determina si hay un camino simple y sin ciclos desde el punto de partida hasta cualquier
#vertice con la condicion de que lo recorra en una distancia de al menos k


def path(exito,u,v,w,suma):
    if exito==True:
        return exito
    for i in range(0,len(edgeList)):
        u=edgeList[i][0]
        v=edgeList[i][1]
        w=edgeList[i][2]
        if u==camino[len(camino)-1] and v not in camino:
            camino.append(v)
            suma+=w
            if suma>=k:
                exito=True
            exito=path(exito, u, v, w, suma)
            suma-=w
            camino.pop()
        elif v==camino[len(camino)-1] and u not in camino:
            camino.append(u)
            suma+=w
            if suma>=k:
                exito=True
            exito=path(exito, u, v, w, suma)
            suma-=w
            camino.pop()
    return exito
        

#edgeList = [[0, 1, 4], [0, 7, 8], [1, 7, 11], [1, 2, 8], [2, 8, 2], [8, 6, 6], 
#                [6, 7, 1], [7, 8, 7], [2, 3, 7], [2, 5, 4], [5, 6, 2], [3, 5, 14], 
#               [3, 4, 9], [4, 5, 10]]
#k=58
edgeList = [[0,1,100], [1,2,200], [2,3,300]]
k = 250
suma=0
camino=[0]
u=[]
v=[]
w=[]
exito= False
print(path(exito,u,v,w,suma))

