"""

Funções - (def) em Python - Escopo
(Parte 4)

"""
# Escopo
variavel = 'valor'  # escopo global


def func():
    print(variavel)


def func2(arg=None):
    # global variavel  # inseri no escopo global (!!NÃO É UMA BOA PRÁTICA!!)
    # variavel = 'Outro valor'  # escopo local
    # print(variavel)

    arg = arg.replace('v', 'c')
    return arg


func()
# func2()
outra_variavel = func2(arg=variavel)

# print(variavel)
print(outra_variavel)

# Ex1 - variável configurada

variavel = 'valor'


def func():
    # print(variavel) # Não pode utilizar antes de config
    variavel = 1234
    print(variavel)


func()

# Ex2 - Variáveis em outras funções

variavel = 'valor'


def func():
    outra_variavel = 'valor'


def func2():
    print(outra_variavel)  # Náo pode usar variável de outra função


func()
func2()

# Ex3 - Integrando funções entre si


def func():
    outra_variavel = 'Rafael Vale'
    return outra_variavel


def func2(arg):
    print(arg)


var = func()
func2(var)
