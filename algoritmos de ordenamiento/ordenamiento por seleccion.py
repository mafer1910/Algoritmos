# -*- coding: utf-8 -*-
"""
Created on Fri Aug 29 13:38:31 2025

@author: MaFer
"""

#ordenamiento por seleccion
#este algoritmo requiere un orden o(n^2) de operaciones para ordenar una lista de n numeros
#este algoritmo encuentra el minimo elemento de la lista, lo intercambia con el primer elemento, busca el minimo del
#resto de la lista, sin contar el primero que ya esta ordenado, y los vuelve a intercambiar
#asi sucesivamente hasta que este ordenada la lista

lista=[5,8,3,9,2,11]
for i in range(0,5):
    min=i
    for j in range(i+1,6):
        if(lista[j]<lista[min]):
            min=j
    aux=lista[i]
    lista[i]=lista[min]
    lista[min]=aux
    print(lista)
