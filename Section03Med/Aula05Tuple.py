"""

Tuplas em Python

"""
#Tupla
from typing import List


t1 = (1,2,3,'a', 'Rafael Vale')

#Tipo da tupla t1
print(type(t1))
#Tupla t1, índice 4
print(t1[4])

#Iteração
for v in t1:
    print(v)
    
# Elementro índice 2 até o último    
print(t1[2:])

#Criar sem parenteses (com vírgula depois)

t2 = 1,2,'a','b',
print(t2)
    
#Concatenar tuplas

t3 = 1,2,'Rafael',4,5
t4 = 6,7,8,9,10
t5 = t3 + t4
print(t5)
n3, n4, n5, *_ = t5
print(n5)

#Repetir valor da tupla

t6 = (1,2,'Rafael',4,5)*20
print(t6)

#Transformar tuplas

t7 = (1,2,3,4,5)
t7 = list(t7)
t7[1] = 3000
t7 = tuple(t7)

print(t7)
