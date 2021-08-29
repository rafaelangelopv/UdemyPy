"""

Expressão condicional com operador OR

"""

nome = input('Qual o seu nome? ')

# if nome:
#   print(nome)
# else:
#   print('Você não digitou nada =((')

print(nome or 'Você não digitou nada = ((')

# Para na primeira verdadeira
print(nome or None or False or 0 or 'Você não digitou nada = ((' or 'another')

# Ex1

a = 0  # False
b = None  # False
c = False  # False
d = []  # False
e = {}  # False
f = 22  # True
g = 'Rafael'  # True

# O or vai verificar até ser True
variavel = a or b or c or d or e or f or g
print(variavel)