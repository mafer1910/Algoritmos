# -*- coding: utf-8 -*-
"""
Created on Tue Sep  9 18:36:49 2025

@author: MaFer
"""
import math

def diferencia(sumaTemp,suma,sub1,sub2,arr,index): 
    if sumaTemp==suma and len(sub1)==math.ceil(len(arr)/2):
        for i in range(0,len(sub1)):
            sub2.remove(sub1[i])
        return sub1[:],sub2[:]  
    for i in range(index,len(arr)):
        sTemp=sumaTemp+arr[i]
        if sTemp<=suma:
            sumaTemp+=arr[i]
            sub1.append(arr[i]) 
            resultado=diferencia(sumaTemp, suma, sub1, sub2,arr, i+1)
            if resultado:    
                return resultado
            sumaTemp-=arr[i]
            sub1.pop()
            
#23 0 -99 4 189 4             
index=0
sub1=[]
#arr = [3, 4, 5, -3, 100, 1, 89, 54, 23, 20]
arr=[26, 41, -34, 12, 0, 98, -99, 4, 189, -1, 4]
sub2=arr[:]
suma=math.ceil(sum(arr)/2)
sumaTemp=0  
print(diferencia(sumaTemp,suma,sub1,sub2,arr,index))
    
    