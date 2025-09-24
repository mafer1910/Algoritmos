# -*- coding: utf-8 -*-
"""
Created on Fri Aug 29 14:26:23 2025

@author: MaFer
"""

#busqueda secuencial
#no importa el orden, solo revisa cada elemento hasta encontrar lo que busca

lista=[1,3,6,7,8,4]
n=10
band=False
i=0
while (band==False and i<len(lista)):
    if lista[i]==n:
        band=True
    i+=1

if band==False:
    print("El numero no esta en el arreglo")
elif(band==True):
    print("Encontrado en la posicion ", i-1)
    
    
        
        
        
        
        
        
        
        
        
    