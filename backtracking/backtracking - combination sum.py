# -*- coding: utf-8 -*-
"""
Created on Fri Sep 12 08:59:19 2025

@author: MaFer
"""

def suma(arr,target,TodasLasSoluciones,index,sumaTemp,solucion):
    if index==len(arr):
        return TodasLasSoluciones        
    for i in range(index,len(arr)):
        if sum(solucion)<=target:
            solucion.append(arr[i])
            solucion.sort()
            if sum(solucion)==target and solucion not in TodasLasSoluciones:
                TodasLasSoluciones.extend([solucion[:]])
            suma(arr, target, TodasLasSoluciones, index, sumaTemp, solucion)
            solucion.pop()
    res=suma(arr, target, TodasLasSoluciones, index+1, sumaTemp, solucion)
    if res:
        return res                    
        
arr=[2, 7, 6, 5]
target=16
index=0
TodasLasSoluciones=[]
sumaTemp=0
solucion=[]
print(suma(arr, target, TodasLasSoluciones,index,sumaTemp,solucion))
