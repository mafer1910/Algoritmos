# -*- coding: utf-8 -*-
"""
Created on Thu Sep 11 11:35:44 2025

@author: MaFer
"""

#8 queens

#el problema es acomodar 8 reinas en un tablero de ajedrez de tal modo q no se ataquen entre ellas
#(una reina ataca en diagonal, a toda su fila y a toda su columna)

def queen(tablero,index):  
    if index==8:
        return tablero
    for fila in range(index,8):
        for columna in range(0,8):
            if (columnas(tablero, columna) and 1 not in tablero[fila] and diagonales(tablero, fila, columna)):
                tablero[fila][columna]=1
                resultado=queen(tablero,index+1)
                if resultado:
                    return resultado
                tablero[fila][columna]=0          

def columnas(tablero,columna):
    for j in range(0,8):
        if tablero[j][columna]==1:
            return False   
    return True

def diagonales(tablero,fila,columna):
    #diagonal abajo-der
    i, j = fila, columna
    while i<8 and j<8:
        if tablero[i][j]==1:
            return False
        i+=1
        j+=1
    #diagonal abajo-izq
    i, j = fila, columna
    while i<8 and 0<=j:
        if tablero[i][j]==1:
            return False
        i+=1
        j-=1
    #diagonal arriba-izq
    i, j = fila, columna
    while 0<=i and 0<=j:
        if tablero[i][j]==1:
            return False
        i-=1
        j-=1
    #diagonal arriba-derecha
    i, j = fila, columna
    while 0<=i and j<8:
        if tablero[i][j]==1:
            return False
        i-=1
        j+=1
    return True
  
tablero=[[],[],[],[],[],[],[],[]]     
for i in range(0,8):    
    for j in range(0,8):
        tablero[j].append(0)
index=0
queen(tablero,index)
for i in range(0,len(tablero)):
    print(tablero[i])