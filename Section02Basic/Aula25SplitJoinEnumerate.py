"""

Split, Join, Enumerate em Python

* Split - Dividir uma string # str
* Join - Juntar uma string # str
* Enumerate - Enumerar elementos da lista # list / iteráveis

"""

# Split

# Ex1 - split
string = "O Brasil é o país do futebol, o Brasil é penta."
lista = string.split(' ')

print(lista)

# Ex2 - split
string = "O Brasil é o país do futebol, o Brasil é penta."
lista_1 = string.split(' ')  # Divide a string usando como referência o espaço
lista_2 = string.split(',')  # Divide a string usando como referência a vírgula

print(lista_1)
print(lista_2)

# Ex3 - split iteraçao
string = "O Brasil é o país do futebol, o Brasil é penta."
lista_1 = string.split(' ')
lista_2 = string.split(',')

for valor in lista_1:
    print(valor)
for valor in lista_2:
    print(valor)

# Ex4 - count
string = "O Brasil é o país do futebol, o Brasil é penta."
lista_1 = string.split(' ')
lista_2 = string.split(',')

for valor in lista_1:
    print(f'A palavra {valor} apareceu {lista_1.count(valor)}x na frase.')

# Ex5 - count
string = "O Brasil é o país do futebol, o Brasil é penta."
lista_1 = string.split(' ')
lista_2 = string.split(',')

palavra = ''
contagem = 0

for valor in lista_1:
    qtd_vezes = lista_1.count(valor)

    if qtd_vezes > contagem:
        contagem = qtd_vezes
        palavra = valor
print(f'A palavra que apareceu mais vezes é {palavra} ({contagem}x)')

# Ex6 - strip capitalize
string = "O Brasil é o país do futebol, o Brasil é penta."
lista_1 = string.split(' ')
lista_2 = string.split(',')

for valor in lista_2:
    print(valor.strip().capitalize())


# Join

string = 'O Brasil é penta.'
lista = string.split(' ')
string2 = ' '.join(lista)

print(string)
print(lista)
print(string2)

# Enumerate

# Ex1 -
string = 'O Brasil é penta.'
lista = string.split(' ')

for indice, valor in enumerate(lista):
    print(indice, valor, lista[indice])

# Ex2
lista = [
    [1, 2],
    [3, 4],
    [5, 6],
]

for v in lista:
    print(v[0], v[1])

# Ex3 = Ex4
lista = [
    [0, 'Rafael'],
    [1, 'Marcella'],
    [2, 'João'],
]

for indice, nome in lista:
    print(indice, nome)

# Ex3 = Ex4
lista = ['Rafael', 'Marcella', 'João']

for indice, nome in enumerate(lista):
    print(indice, nome)

# Ex5
lista = ['Rafael', 'Marcella', 'João']

n1, n2, n3 = lista

print(n2)

"""

* Enumerate - Enumerar elementos da lista # list

Aula tira dúvidas

"""

lista = [
    # 0          1           2
    ['Rafael', 'Marcella', 'João'],  # 0
    ['Marina', 'Clara', 'Pedro'],  # 1
    ['Ma', 'Cla', 'Pe']  # 2
]

print(lista[2][1])  # Cla

enumerada = enumerate(lista)
print(list(enumerada))  # typecast para lista

"""
[ <-- Enumerate

    #0  1          2           3  
    (0, ['Rafael', 'Marcella', 'João']), #0
        #0         1        2
    (1, ['Marina', 'Clara', 'Pedro']), #1
    (2, ['Ma', 'Cla', 'Pe']) #2
]

"""
# 01
lista = [
    # 0         1           2
    ['Rafael', 'Marcella', 'João'],  # 0
    ['Marina', 'Clara', 'Pedro'],  # 1
    ['Ma', 'Cla', 'Pe']  # 2
]
enumerada = list(enumerate(lista))  # typecast para lista
print(enumerada[1][1][2])

# 02
lista = [
    # 0         1           2
    ['Rafael', 'Marcella', 'João'],  # 0
    ['Marina', 'Clara', 'Pedro'],  # 1
    ['Ma', 'Cla', 'Pe']  # 2
]
for v1, v2 in enumerate(lista, 53):
    print(v1, v2)

# 03
lista = [
    # 0         1           2
    ['Rafael', 'Marcella', 'João'],  # 0
    ['Marina', 'Clara', 'Pedro'],  # 1
    ['Ma', 'Cla', 'Pe']  # 2
]
for v1 in enumerate(lista, 53):
    print(v1)

# 04
lista = [
    # 0         1           2
    ['Rafael', 'Marcella', 'João'],  # 0
    ['Marina', 'Clara', 'Pedro'],  # 1
    ['Ma', 'Cla', 'Pe']  # 2
]
for v1 in enumerate(lista, 53):
    valor_enumerado, minha_lista = v1
    nome1, nome2, nome3 = minha_lista

    print(valor_enumerado, minha_lista)
    print(nome1, nome2, nome3)
