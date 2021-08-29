"""

Unpacking - Desempacotamento de listas em Python

"""

lista = ['Rafael', 'Marcella', 'João', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# _ // O uso do underline siginifica que eu nao vou utilizar esta variável no restante do code,  ou seja, serviu apenas para nomear algo que não tem um significado maior.
n1, n2, n3, *_, ultimo = lista

print(n1, n2, n3, ultimo)
print(ultimo)
