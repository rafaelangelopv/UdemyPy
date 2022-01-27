"""

Funções - (def) em Python - Escopo
(Parte 4)

"""
"""
1 - Crie uma função1 que recebe uma função2 como parâmetro e retorne o valor da
função2 executada.
"""


def msg():
    return 'Hello World!'


def funcao1(funcao2):
    return funcao2()


exec = funcao1(msg)  # A 'funcao1' recebe 'msg' e executa através da  'funcao2'
print(exec)
# print(msg()) #Retorna o mesmo resultado

"""
2 - Crie uma função1 que recebe uma função2 como parâmetro e retorne o valor da
função2 executada. Faça a função1 executar duas funções que recebam um número 
diferente de argumentos.
"""


def funcao1(funcao2, *args, **kwargs):
    # recebe a funcao2 e todos os argumentos restantes
    return funcao2(*args, **kwargs)
    # retorna a funcao2 e todos os argumentos restantes


def fala(nome):
    return f'Oi {nome}'


def saudacao(nome, saudacao):
    return f'{saudacao} {nome}'


exec1 = funcao1(fala, 'Rafael')
# exec1 recebe funcao1 com o argumento fala (que é uma função retornando 'Oi {nome}) e 'Rafael', que é atribuído ao nome.
# A funcao1 é executada através da funcao2 que também retorna args e kwargs.
exec2 = funcao1(saudacao, 'Rafael', saudacao='Bom dia!')
print(exec1)
print(exec2)
