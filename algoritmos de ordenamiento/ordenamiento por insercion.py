# -*- coding: utf-8 -*-
"""
Created on Fri Aug 29 10:54:39 2025

@author: MaFer
"""
#ordenamiento por insercion
#parte desde la posicion 1, compara el numero que esta a la izquierda y si es menor
#entonces esta ordenado, caso contrario se hace el intercambio, requiere un orden O(n^2)
#operaciones para ordenar un arreglo de n elementos

lista=[5,8,3,9,2,11]
for i in range(1,6):
    pos=i
    aux=lista[i]
    while(pos>0 and aux<lista[pos-1]):
        lista[pos]=lista[pos-1]
        pos-=1
    lista[pos]=aux
print(lista)
        