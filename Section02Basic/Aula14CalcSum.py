"""

Documentação importante

https://docs.python.org/3/library/stdtypes.html
https://github.com/luizomf/check-numbers-python/blob/master/chk_numbers.py

Funções: isnumeric isdigit isdecimal

"""
##-----------------------------------Explicação Inicial-----------------------------------##
##-----------------------------------Da erro se digitar letras----------------------------##


# num1 = input('Digite um número: ')
# num2 = input('Digite outro número número: ')

# num1 = int(num1)
# num2 = int(num2)
# print(num1 + num2)

# # Somente números e positivos
# print(num1.isnumeric())
# print(num2.isnumeric())

##-----------------------------------Calculadora----------------------------------------------------##
##---Verifica primeiro se é número para depois transformar para inteiro e conseguir fazer a conta---##

# num1 = input('Digite um número: ')
# num2 = input('Ditite outro número: ')

# if num1.isdigit() and num2.isdigit():
#     num1 = int(num1)
#     num2 = int(num2)

#     print('\n'*3)
#     print(num1 + num2)
# else:
#     print('Não pude converter os números para realizar contas..')


# ##-----------------------------------Funções Importantes-----------------------------------##
# ##----- https://github.com/luizomf/check-numbers-python/blob/master/chk_numbers.py---------##

import re
# String para Float


def is_float(val):
    if isinstance(val, float):
        return True
    if re.search(r'^\-{,1}[0-9]+\.{1}[0-9]+$', val):
        return True

    return False

# String para Int


def is_int(val):
    if isinstance(val, int):
        return True
    if re.search(r'^\-{,1}[0-9]+$', val):
        return True

    return False

# String para Numbers in general (float ou int)


def is_number(val):
    return is_int(val) or is_float(val)

###########
#  USAGE  #
###########


# # Float
# print(is_float('-101.0112'))  # True
# # Int
# print(is_int('-1010112'))  # True
# # Numbers in general (float ou int)
# print(is_number('-1010.112'))  # True

# # False
# print(is_number('123a'))  # False

num1 = input('Digite um número: ')
num2 = input('Digite outro número: ')

# É necessário criar as funções acima primeiro, os código tem que estar ativos

if is_number(num1) and is_number(num2):  # Verifica se é um número int ou float

    num1 = float(num1)
    num2 = float(num2)

    print(num1 + num2)
else:
    print('ERROR')

##-----------------------------------Outra forma-----------------------------------##

num1 = input('Digite um número: ')
num2 = input('Digite outro número: ')
try:
    num1 = float(num1)
    num2 = float(num2)

    print(num1 + num2)
except:
    print('ERROR')
