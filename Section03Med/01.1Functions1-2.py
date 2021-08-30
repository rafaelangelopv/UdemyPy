"""

Funções - (def) em Python (Parte 1 / Parte 2)

"""
# Funçao


def funcao():
    print('Hello World!')


funcao()

# Funcao - Parametros


def saudacao(msg='Olá', nome='usuário'):
    nome = nome.replace('e', '3')
    msg = msg.replace('e', '3')
    print(msg, nome)


saudacao()
saudacao(nome='Rafael')
saudacao(nome='Rafael', msg='Hi')
saudacao('Olá', 'Rafael Angelo')
saudacao('Oi', 'Marcella')
saudacao('Bom dia', 'Joao')
saudacao('Boa tarde', 'Angelo')

# Funcao - Return


def saudacao(msg='Olá', nome='usuário'):
    nome = nome.replace('e', '3')
    msg = msg.replace('e', '3')
    return f'{msg} {nome}'


variavel = saudacao()

print(variavel)

# Funcao - Return (continue)


def funcao(var):
    return var
    print('Isso não será executado.')


variavel = funcao('Valor que eu quero.')

if variavel:
    print(variavel)
else:
    print('Nenhum valor.')

# Funcao - Divisão


def divisao(n1, n2):
    if n2 == 0:
        return

    return n1/n2


divide = divisao(8, 4)
if divide:
    print(divide)
else:
    print('Conta inválida.')

# Funcao - Tipos


def dumb():
    return 1


var = dumb()
print(var, type(var))

# Funcao - Tuplas


def dumb():
    return ('Rafael', 'Angelo')


var = dumb()
print(dumb())  # lista
print(var[1], type(var))  # tupla // não pode ser alterada
