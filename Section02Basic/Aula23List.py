"""

Listas em Python
fatiamento
append, insert, pop, del, clear, extend, +
min, max
range

"""
#         0    1    2    3    4   5
lista = ['A', 'B', 'C', 'D', 'E', 10.5]
lista[5] = 'Another'
print(lista[5])


# Fatiamento

#         0    1    2    3    4   5
lista = ['A', 'B', 'C', 'D', 'E', 10.5]
print(lista[0])  # primeiro
#         0    1    2    3    4   5
lista = ['A', 'B', 'C', 'D', 'E', 10.5]
print(lista[:3])  # até o terceiro
#         0    1    2    3    4   5
lista = ['A', 'B', 'C', 'D', 'E', 10.5]
print(lista[0:3])  # até o terceiro
#         0    1    2    3    4   5
lista = ['A', 'B', 'C', 'D', 'E', 10.5]
print(lista[1:4])  # 2o ao 3o
#         0    1    2    3    4   5
lista = ['A', 'B', 'C', 'D', 'E', 10.5]
print(lista[2:])  # 20 ao final
#         0    1    2    3    4   5
lista = ['A', 'B', 'C', 'D', 'E', 10.5]
print(lista[-1])  # inverso/ultimo
#         0    1    2    3    4   5
lista = ['A', 'B', 'C', 'D', 'E', 10.5]
print(lista[::2])  # step de 2 em 2
#         0    1    2    3    4   5
lista = ['A', 'B', 'C', 'D', 'E', 10.5]
print(lista[::-1])  # inverso até o inicio


# Funções

l1 = [1, 2, 3]
l2 = [4, 5, 6]
l3 = l1 + l2  # concatenar
print(l1)
print(l2)
print(l3)

# Extend

l1 = [1, 2, 3]
l2 = [4, 5, 6]
l1.extend(l2)  # adiciona os valores da l2 na l1
l1.extend('a')  # adiciona a na lista l1
print(l1)
print(l2)

# Append

l1 = [1, 2, 3]
l2 = [4, 5, 6]
l2.append('b')  # insere o valor no final da lista
print(l1)
print(l2)

# Insert

l1 = [1, 2, 3]
l2 = [4, 5, 6]
l2.insert(0, 'b')  # insere o valor no indice indicado
print(l1)
print(l2)

# Pop

l2 = [4, 5, 6]
print(l2)
l2.insert(0, 'b')
print(l2)
l2.pop()
print(l2)  # exclui o ultimo indice

# Del

#     0  1  2  3  4  5  6  7  8
l2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
del(l2[3:5])  # exclui um trecho
print(l2)

#     0  1  2  3  4  5  6  7  8
l2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(l2)
l2.insert(0, 'b')  # inserir 'b' no indice 0
print(l2)
del(l2[0])  # exclui o indice 0
print(l2)

# Min & Max

#     0  1  2  3  4  5  6  7  8
l2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(min(l2))
print(max(l2))

# Range - List built-in

l2 = list(range(1, 10))  # cria uma lista de 1 a 9
print(l2)
l2 = list(range(0, 100, 8))  # cria uma lista de 0 a 10 com steps de 8
print(l2)


# Tipos

l2 = ['String', True, 10, -20.5]
for elem in l2:
    print(f'O tipo de elem é {type(elem)} e seu valor é {elem}')


#### jogo_adivinhacao.py ####
