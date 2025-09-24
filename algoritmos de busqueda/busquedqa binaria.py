# -*- coding: utf-8 -*-
"""
Created on Fri Aug 29 23:24:53 2025

@author: MaFer
"""

#busqueda binaria
#LA LISTA DEBE ESTAR ORDENADA
#parte el arreglo a la mitad y si el numero se encuentra a la mitad termina el ciclo, pues ya encontro el numero
#caso contrario lo vuelve a partir a la mitad preguntando si el numero es mayor o menor a la mitad, si es mayor
#entonces pertenece a la mitad superior, si es menor pertenece a la inferior, 
#con respecto a esa mitad se repite el proceso

lista=[1,2,3,4,5,6]
n=3
inf=0
sup=len(lista)
band=False
while(n>=lista[inf] and n<=sup):
    mitad=int((inf+sup)/2)
    if lista[mitad]==n:
        band=True
        break
    elif lista[mitad]<n:
        inf=mitad
        mitad=int((inf+sup)/2)
    elif lista[mitad]>n:
        sup=mitad
        mitad=int((inf+sup)/2)
if band==False:
    print("el numero no esta en el arreglo")
elif(band==True):
    print("encontrado en la posicion ", mitad)