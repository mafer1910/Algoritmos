# -*- coding: utf-8 -*-
"""
Created on Sat Sep  6 01:11:19 2025

@author: MaFer
"""

#subsets para un array de longitud n

def subsets(index,s,res,temp):
    temp.sort()
    if not temp in res:
        res.append(temp[:])
    
    for i in range(index,len(s)):
        #selecciona nueva opcion
        if not s[i] in temp:
            temp.append(s[i])        
            #si es aceptable, la anota, es decir todas pq en este problema no hay restricciones
            subsets(index+1,s,res,temp)            
            temp.remove(s[i])
    
   
index=0
s=[1,2,3]
temp=[] 
res=[]
subsets(index,s,res,temp)
print(res)