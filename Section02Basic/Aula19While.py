"""

While (enquanto) 
em Python

Utilizado para ações enquanto uma condição for verdadeira

Requisitos: Entender condições e operadores

"""

while True:  # loop infinito
    nome = input("Qual o seu nome? ")
    print(f'Olá {nome}!')

print('Não será executada.')

# 0 até 10 com 'continue'
x = 0

while x < 10:
    if x == 3:  # pula o 3 com o uso do continue
        x = x + 1
        continue  # pula par ao proximo laço

    print(x)
    x = x + 1

print('Acabou!')

# 0 até 10 com 'break'
x = 0

while x < 10:
    if x == 3:  # pula o 3 com o uso do continue
        x = x + 1
        break  # finaliza o laço

    print(x)
    x = x + 1

print('Acabou!')

# Exemplo coordenadas

x = 0  # coluna

while x < 10:
    y = 0  # linha

    while y < 5:
        print(f'({x},{y})')  # coordenadas
        y += 1

    x += 1  # x = x + 1

print('Acabou!')

# Exemplo calculadora simples

while True:
    print()
    num_1 = input('Digite um número: ')
    num_2 = input('Digite outro número: ')
    operador = input('Digite um operador: ')

    if not num_1.isnumeric() or not num_2.isnumeric():
        print('Você precisa digitar um número')
        continue

    num_1 = int(num_1)
    num_2 = int(num_2)

    # + - / *
    if operador == '+':
        print(num_1 + num_2)
    elif operador == '-':
        print(num_1 - num_2)
    elif operador == '/':
        print(num_1 / num_2)
    elif operador == '*':
        print(num_1 * num_2)
    else:
        print('Operador inválido!')

    sair = input('Deseja sair? [s]im ou [n]ão: ')

    if sair == 's':
        break
