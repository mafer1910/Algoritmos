# -*- coding: utf-8 -*-
"""
Created on Thu Sep 25 19:10:00 2025

@author: MaFer
"""

#non-decreasing substring

def substring(arr):
    i=0
    j=1
    max=0
    while(j<len(arr)-1):
        j+=1
        if arr[j]<arr[j-1]:  
            if len(arr[i:j])>max:
                max=len(arr[i:j])
                i=j
        elif j==(len(arr)-1):
            if len(arr[i:j+1])>max:
                max=len(arr[i:j+1])
                i=j            
    return max
    
arr=[2, 2, 1, 3, 4, 1]
print(substring(arr))