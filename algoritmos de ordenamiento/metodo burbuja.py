# -*- coding: utf-8 -*-
"""
Created on Fri Aug 29 00:03:25 2025

@author: MaFer
"""

#metodos de ordenamiento: metodo burbuja

#revisa cada elemento de la lista comparandolo con el siguiente y los intercambia si estan en orden incorrecto. 
#Es necesario revisar varias veces toda la lista hasta que no se necesiten mas intercambio, en ese caso ya estara ordenada


lista=[12,56,43,3,8,34]
aux=0
for i in range(0,5):
    for j in range(0,5):
        if (lista[j]>lista[j+1]):
            aux=lista[j]
            lista[j]=lista[j+1]
            lista[j+1]=aux
print(lista)