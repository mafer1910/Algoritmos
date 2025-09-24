# -*- coding: utf-8 -*-
"""
Created on Wed Sep  3 15:04:09 2025

@author: MaFer
"""

#recursion para permutaciones de una cadena ABC


def permutar(index, s, ans): 
    if index==len(s):
        ans.append("".join(s))
        return 
    for i in range(index,len(s)):
        s[index],s[i]=s[i],s[index]
        permutar(index + 1, s, ans)
        s[index],s[i]=s[i],s[index]
        

s="ABCD"
ans=[]
permutar(0, list(s), ans)
print(ans)