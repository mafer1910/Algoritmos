# -*- coding: utf-8 -*-
"""
Created on Sat Sep 13 01:26:12 2025

@author: MaFer
"""

#problema del caballo de ajedrez
def caballo(tablero, index, i, j, casillas,movimientos,ultimoMov): 
    if index==64:
        return tablero[:]
    for a in range(index,64):
        if index>0:
            ultimoMov=movimientos[len(movimientos)-1]
            movimientos=[]
        for opcion in range(0,len(casillas)): 
            tablero[i][j]=index
            movimiento=visitado(tablero,i,j,opcion,ultimoMov)
            movimientos.append(opcion)
            if movimiento:
                print(index,opcion,i,j,a)
                SigCasilla=casillas[movimiento]
                i+=SigCasilla[0]
                j+=SigCasilla[1]
                res=caballo(tablero, index+1, i, j, casillas,movimientos,ultimoMov) 
                if res:
                    return res[:]
        a-=1
        index-=1
        tablero[i][j]=0            
        
        
                
              
def visitado(tablero,i,j,opcion,ultimoMov): 
    if opcion!=ultimoMov:
        #abajo-derecha
            if opcion==0:
                if i<=5 and j<=6 and tablero[i+2][j+1]==0:
                    return 0
                
            if opcion==1:
                if i<=6 and j<=5 and tablero[i+1][j+2]==0:
                    return 1
            
            #arriba-derecha
            if opcion==2:
                if i>=1 and j<=5 and tablero[i-1][j+2]==0:
                    return 2
            if opcion==3:
                if i>=2 and j<=6 and tablero[i-2][j+1]==0:
                    return 3
            
            #abajo-izquierda
            if opcion==4:
                if i<=5 and j>=1 and tablero[i+2][j-1]==0:
                    return 4
            if opcion==5:
                if i<=6 and j>=2 and tablero[i+1][j-2]==0:
                    return 5
                
            #arriba-izq
            if opcion==6:
                if i>=2 and j>=1 and tablero[i-2][j-1]==0:
                    return 6
            if opcion==7:
                if i>=1 and j>=2 and tablero[i-1][j-2]==0:
                    return 7
    

#definimos el tablero y lo llenamos de ceros, conforme se va ocupango un lugar se suma 1 hasta llegar a las 64 casillas, 63 pues inicia en 0
tablero=[[],[],[],[],[],[],[],[]]  
for i in range(0,8):    
    for j in range(0,8):
        tablero[j].append(0) 
#se inicializa la primera casilla visitada [0,0] en 0, comienza la cuenta
index=0
#mediante el metodo 'visitado' se define la ubicacion de la siguiente  casilla, sumando o restando respectivamente 
#de siguiendo las reglas de movimiento del caballo y verificando q la casilla este vacia
casillas=[[2,1],[1,2],[-1,2],[-2,1],[2,-1],[1,-2],[-2,-1],[-1,-2]]
opcionesVisitadasSinExito=[]
#posicion actual
i=0
j=0
#posicion anterior
viejafil=0
viejacol=0
movimientos=[]
ultimoMov=None
caballo(tablero, index, i, j, casillas,movimientos,ultimoMov) 
for b in range(0,len(tablero)):
    print(tablero[b])
    
    
    
# tablero[i][j]=index   
# nuevapos=visitado(tablero,tableroVisitado, i, j,index)
# if nuevapos: 
#     if index!=0 and tablero[i][j]!=0:                
#         tableroVisitado[i][j]='V'
#     print([nuevapos[0],nuevapos[1]],[i,j],[viejafil,viejacol],index)
#     viejafil=i
#     viejacol=j                       
#     i=nuevapos[0]
#     j=nuevapos[1]
#     res=caballo(tablero,tableroVisitado, index+1,i,j,viejafil,viejacol)
#     if res:
#         return res
#     index-=1
#     tablero[i][j]=0
#     tableroVisitado[i][j]='V'            
#     i=viejafil
#     j=viejacol
# break