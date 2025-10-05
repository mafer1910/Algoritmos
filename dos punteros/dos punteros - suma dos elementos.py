# -*- coding: utf-8 -*-
"""
Created on Thu Sep 25 01:51:35 2025

@author: MaFer
"""

#encontrar dos elementos del arreglo cuya suma sea igual a un valor objetivo x utilizando la tecnica de los dos punteros


def sumax(arr):
    i=0
    j=len(arr)-1
    suma=arr[i]+arr[j]
    while suma!=x:
        if suma>x:
            j-=1
        elif suma<x:
            i+=1
        suma=arr[i]+arr[j]
    return [i,j]
    
arr=[1, 3, 2, 5, 1, 1, 2, 3]
arr.sort()
x=8
print(sumax(arr))