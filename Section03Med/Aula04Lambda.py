"""

Funções Lambda ou Expressões Lambda

"""

# funcao padrao, standart


def funcao(arg, arg2):
    return arg*arg


var = funcao(2, 2)
print('EXEMPLO 01')
print(var)

# funcao lambda, expressão labda


def a(x, y): return x*y


print('EXEMPLO 02')
print(a(2, 2))


# Exemplo padrão

lista = [
    ['P1', 13],
    ['P2', 6],
    ['P3', 7],
    ['P4', 50],
    ['P5', 8],
]


def func(item):
    return item[1]


lista.sort(key=func)
print('EXEMPLO 03')
print(lista)

lista.sort(key=func, reverse=True)
print('EXEMPLO 04')
print(lista)

# Exemplo lambda

lista = [
    ['P1', 13],
    ['P2', 6],
    ['P3', 7],
    ['P4', 50],
    ['P5', 8],
]

lista.sort(key=lambda item: item[1])
print('EXEMPLO 05')
print(lista)

lista.sort(key=lambda item: item[1], reverse=True)
print('EXEMPLO 06')
print(lista)


# ordenar com sorted + lambda

lista = [
    ['P1', 13],
    ['P2', 6],
    ['P3', 7],
    ['P4', 50],
    ['P5', 8],
]
print('EXEMPLO 07')
print(sorted(lista))

print('EXEMPLO 08')
print(sorted(lista, key=lambda i: i[1]))

print('EXEMPLO 09')
print(sorted(lista, key=lambda i: i[1], reverse=True))

print('EXEMPLO 10')
# ordenar pelo nome do produto/inverso
print(sorted(lista, key=lambda i: i[0], reverse=True))
