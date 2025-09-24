# -*- coding: utf-8 -*-
"""
Created on Thu Sep  4 23:50:26 2025

@author: MaFer
"""

#checa por una sum-string: esto es si una string puede ser dividida en mas de dos strings 
#y la inmediata a esas dos strings anteriores debe ser igual a la suma de estas dos strings q le 
#anteceden. Esta regla solo aplica a la string que le antecede

   
def sumString(s,index,exito,prevsum,prev2):
    if index==len(s)-len(prevsum[0])-len(prev2[0]):
        print('b')
        return True
    for i in range(index+1,len(s)+1):
        for j in range(i+1,len(s)+1):
            for k in range(j+1,len(s)+1):
                n1=s[index:i]
                n2=s[i:j]
                suma=s[j:k] 
                print(n1,n2,suma)
                if int(n1)+int(n2)==int(suma):
                    if int(suma)>int(prevsum[0]): 
                        print('si')
                        prevsum[0]=suma
                        prev2[0]=n2
                        exito=sumString(s,index+len(n1),exito,prevsum,prev2)
    return exito
                

index=0
s = "1111112223335558"
exito=False
prevsum=['0']
prev2=['0']
print(sumString(s,index,exito,prevsum,prev2))


