"""

Formatando valores com modificadores

:s - Texto (strings)
:d - Inteiros (int)
:f - Números de ponto flutuante (float)
:.(NÚMERO)f ( > ou < ) (QUANTIDADE) (TIPO - s, d ou f)
(\n) pula uma linha

> - Esquerda (local onde os números serão adicionados)
< - Direita (local onde os números serão adicionados)
^ - Centro (local onde o número será colocado)

"""

num_1 = 10
num_2 = 3
divisao = num_1 / num_2
print('{:.2f}'.format(divisao))  # :.2f para duas casas decimais
print(f'{divisao:.2f}')

nome = 'Rafael Angelo'
print(f'{nome:s}')  # :s - string, o mesmo para :d e :f

num_3 = 1
# :0>10 serão 10 números no total,9 zeros adicionados a esqueda.
print(f'{num_3:0>10}')

num_4 = 1150
# :0>10 serão 10 números no total,6 zeros adicionados a esqueda.
print(f'{num_4:0>10}')
print(f'{num_4:.2f}')  # transformando em float com duas casas
print(f'{num_4:0>10.2f}')  # totaliza os 10 digitos, contando com o ponto

nome = 'Rafael Vale'
print((50-len(nome)) / 2)
# adiciona # até completar 50 caracteres com o nome no centro ^
print(f'{nome:#^50}')

nome = 'Rafael Vale'
nome_formatado = '{:@>50}'.format(nome)
# adiciona @ até completar 50 caracteres, a esquerda.
print(nome_formatado)

nome = 'Rafael Vale'
nome_formatado = '{n:0<20}'.format(n=nome)
# adiciona zeros até completar 20 caracteres, a direita.
print(nome_formatado)

nome = 'Rafael Angelo'
sobrenome = 'Pinheiro do Vale'
nome_formatado = '{0:$^50}\n{1:#^50}'.format(nome, sobrenome)
# adiciona $ no nome e # no sobrenome, até completar 50 caracteres, o nome e sobrenome ficarão no centro ^
print(nome_formatado)

nome = 'Rafael angelo PiNhEiRo'
# justifica o nome a esquerda left just e preenche com # até 20 caractéries
nome = nome.ljust(20, '#')

print(nome)
print(nome.lower())  # tudo minúsculo
print(nome.upper())  # tudo maiúsculo
print(nome.title())  # Primeiras letras maiúsculas
