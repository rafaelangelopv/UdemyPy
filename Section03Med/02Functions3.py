"""

Funções - (def) em Python - *args **kwargs
(Parte 3)

"""

# Funções


from collections import namedtuple


def fun(a1, a2, a3, a4, a5, nome=None, a6=None):
    print(a1, a2, a3, a4, a5, nome, a6)
    return nome, a6


var = fun(1, 2, 3, 4, 5, nome='Rafael', a6=6)
print(var[0], var[1])

#Ex1 - args


def func(*args):
    args = list(args)
    args[0] = 20
    print(args)
    print(args[0])
    print(args[-1])
    print(len(args))


lista = [1, 2, 3, 4, 5]
#n1, n2, *n = lista
#print(n1, n2, n)
# print(*lista, sep='-') #unpacked and -
func(1, 2, 3, 4, 5)  # tupla

# Ex2 - args, kwargs


def func(*args, **kwargs):
    #    for v in args:
    #        print(v)
    print(args)
    # print(kwargs['name'], kwargs['lastname'])

    # name = kwargs.get('name')
    # print(name)

    yrs = kwargs.get('yrs')

    if yrs is not None:
        print(yrs)
    else:
        print('Idade não existe')


lista = [1, 2, 3, 4, 5]
lista2 = [10, 20, 30, 40, 50]
func(*lista, *lista2, name='Rafael', lastname='Vale', yrs=30)
