# -*- coding: utf-8 -*-
"""
Created on Mon Sep  1 00:11:10 2025

@author: MaFer
"""

def fibo(n):
    if n==1:
        resultado=0
    elif n==2:
        resultado=1
    else: 
        resultado=fibo(n-1)+fibo(n-2)
    return resultado
print(fibo(10))