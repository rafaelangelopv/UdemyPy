"""

Operador ternário em Python

"""
# Forma padrão
logged_user = True

if logged_user:
    msg = 'Usuário logado.'
else:
    msg = 'Usuário precisa logar.'

print(msg)

# com Operador Ternário

logged_user = True
msg = 'Usuário logado.' if logged_user else 'Usuário precisa logar.'

print(msg)

# Ex1
idade = input('Qual a sua idade? ')

if not idade.isnumeric():
  print('Voce precisa digitar apenas números!')
else:
  idade = int(idade)
  maior = (idade >= 18)

# if idade >= 18:
#     print('Pode acessar.')
# else:
#     print('Não pode acessar.')

  msg = 'Pode acessar.' if maior else 'Não pode acessar.'

  print(msg)
