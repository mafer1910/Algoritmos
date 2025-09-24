# -*- coding: utf-8 -*-
"""
Created on Sat Sep  6 20:20:25 2025

@author: MaFer
"""

def path(index,n,edgeList,source,destination):
    if temp[len(temp)-1]==destination:
        return 1
    p=0
    for i in range(index,len(edgeList)):
        if edgeList[i][0]==temp[len(temp)-1]:
            temp.append(edgeList[i][1])
            p+=path(index+1, n, edgeList, source, destination)
            temp.pop()
    return p

n = 5
edgeList = [['A', 'B'], ['A', 'C'], ['A', 'E'], ['B', 'E'], ['B', 'D'], ['C', 'E'], ['D', 'C']]
source = 'A' 
temp=['A']
destination = 'E'
print(path(0, n, edgeList, source, destination))

        
        