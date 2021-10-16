"""

FOR / ELSE em Python

"""

# Ex1 - iteraçao continue and break
variavel = ('Rafael Angelo', 'Marcella Parente', 'Joao')
for valor in variavel:
    print(valor)
    break
    print(valor)

# Ex2 - iteraçao valor.startswith
variavel = ('Rafael Angelo', 'Marcella Parente', 'Joao')
for valor in variavel:
    if valor.startswith('J'):
        print('Começa com J', valor)
    else:
        print('Não começa com J', valor)

# Ex3 - iteraçao com variavel verificaçao
variavel = ('Rafael Angelo', 'Marcella Parente', 'Joao')
comeca_com_j = False
for valor in variavel:
    if valor.lower().startswith('j'):
        comeca_com_j = True
if comeca_com_j:
    print('Existe uma palavra que começa com J.')
else:
    print('Não existe uma palavra que começa com J.')

# Ex4 - iteraçao com variavel verificaçao - for else
variavel = ('Rafael Angelo', 'Marcella Parente', 'Joao')

for valor in variavel:
    if valor.lower().startswith('j'):
        break
else:
    print('Não existe uma palavra que começa com J.')
