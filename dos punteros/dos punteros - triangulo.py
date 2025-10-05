# -*- coding: utf-8 -*-
"""
Created on Fri Sep 26 14:21:54 2025

@author: MaFer
"""
#problem: determine if a triangle or a degenerated triangle can be formed using 4 sticks (one is extra), 
#whose lengths are represented by integers in the array 'arr'

#solucion rapida
def triangulo(arr):
    a=0
    b=2
    i=0
    j=2
    while b<4: #comprueba si es triangulo
        temp=arr[a:b+1]
        if temp[2]>(temp[1]-temp[0]) and temp[2]<(temp[1]+temp[0]):
            return 'TRIANGLE'
        else:                
            a+=1
            b+=1
    #se reinicia al comprobar q no es posible formar un triangulo entonces sigue a comprobar si es degenerado o imposible            
    while j<4: #comprueba si es degenerado
        temp=arr[i:j+1]
        if (temp[0]+temp[1])==temp[2] or (temp[0]+temp[2])==temp[1] or (temp[2]+temp[1])==temp[0]:
            return 'SEGMENT'
        else:               
            i+=1
            j+=1
    #se comprobo q no es posible formar un triangulo ni degenereado, por lo que regresa imposible            
    return 'IMPOSSIBLE'

#solucion optima
def triangulo2(arr):
    i=0
    j=2
    while j<4:
        a,b,c=arr[i],arr[i+1],arr[j]
        if c>(b-a) and c<(a+b):
            return 'TRIANGULO'
        elif (a+b)==c:
            return 'SEGMENTO'
        j+=1 #recorre el subsegmento a la derecha, descartando el primer lado, si la siguiente
        i+=1 #iteracion demuestra que no es triangulo ni degenerado entonces regresa imposible pues no hay mas lados que comparar
    return 'IMPOSIBLE'        
      
  
arr=[7, 2, 2, 4]
arr.sort()
print(triangulo2(arr))