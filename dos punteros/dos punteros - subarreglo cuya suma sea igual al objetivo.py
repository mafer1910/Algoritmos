# -*- coding: utf-8 -*-
"""
Created on Thu Sep 25 02:03:25 2025

@author: MaFer
"""

#encontrar un subarreglo cuya suma sea igual a un valor objetivo x utilizando la tecnica de los dos punteros

def sumax(arr):
    i=0
    j=0
    suma=0
    while i<len(arr):
        if suma<x:
            suma+=arr[i]
            i+=1
        elif suma>x:
            suma-=arr[j]
            j+=1
        elif suma==x:            
            return arr[j:i]        
    return False
    
arr=[1, 3, 2, 5, 1, 1, 2, 3]
x=8
resultado=sumax(arr)
if resultado:
    print(resultado)
else:
    print('Arreglo no encontrado')
