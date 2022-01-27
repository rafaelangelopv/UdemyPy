"""

Dicionários em Python

"""
#Chave Valor

d1 = {'chave1':'valor da chave'}
print(type(d1))
print(d1)

d1['nova_chave'] = 'Valor da nova'
print(d1['chave1'])
print(d1['nova_chave'])

d1 = dict(chave1 = 'Valor da chave', chave2 = 'Valor da outra chave')
print(d1)

# Estrutura mais comum para dicionários

#d1 = {'chave': 'valor','chave' : 'valor'}
    # d1 = {'key': 'value','key': 'value'}
    #print(d1)

d1 = { 1: 'valor', 2: 'valor', 3: 'valor real da chave'}
    # d1 = {'key': 'value','key': 'value'}
print(d1)
print(d1[3])

# Chaves

d1 = {
    'str' : 'valor',
    123: 'Outro valor',
    (1,2,3,4) : 'Tupla',   
}

d1['naoexiste'] = 'Agora existe.'
if 'naoexiste' in d1:
    print (d1['naoexiste'])
print('texto depois do dicionário')

print(d1.get('nomedachave')) #None


# Maneira de atualizar

#01
d1['nomedachave'] = 'Agora ela existe'
if d1.get('nomedachave') is not None:
    print(d1.get('nomedachave'))
print('texto depois do dicionário')

#02
d1.update({'nova_chave':'novo_valor'})
if d1.get('nova_chave') is not None:
    print(d1.get('nova_chave'))
print('texto depois do dicionário')

# Apagar

del d1['str']
print(d1)

# Encontrar valores dentro do dicionário

d2 = {
    'str' : 'valor',
    123: 'Outro valor',
    (1,2,3,4) : 'Tupla',   
}

print('str' in d2)
print('str' in d2.keys())
print('valor' in d2.values())

# Quantidade de pares (chave:valor) no dicionário

d2 = {
    'str' : 'valor',
    123: 'Outro valor',
    (1,2,3,4) : 'Tupla',   
}

print(len(d2))

# Iteraçao


d2 = {
    'chave1' : 'valor',
    'chave2' : 'Outro valor',
    'chave3' : 'Tupla',   
}

#chave
for k in d2:
    print(k)

#valor    
for v in d2.values():
    print(v)

#chave e valor    
for k in d2.items():
    print(k[0], k[1])
    
#desempacotar

for k, v in d2.items():
    print(k, v)
    
    
    
    
#Dicionário dentro de dicionários (iterações)

clientes = {
    'cliente1' : {
         'nome' : 'Rafael',
         'sobrenome' : 'Angelo',
    },
     'cliente2' : {
         'nome' : 'Marcella',
         'sobrenome' : 'Parente',
    },
}

for clientes_k, clientes_v in clientes.items():
    print(f'Exibindo {clientes_k}')
    for dados_k, dados_v in clientes_v.items():
        print(f'\t{dados_k} = {dados_v}')
        
        
        
# Cópia raza

d3 = { 1: 'a', 2: 'b', 3: 'c', 'd' : ['Pinheiro', 'do Vale']}
v = d3.copy()

v[1] = 'Rafael'
v['d'][0] = 'Parente'

print(d3)
print(v)

# Cópia profunda

import copy as cpy

d3 = { 1: 'a', 2: 'b', 3: 'c', 'd' : ['Pinheiro', 'do Vale']}
v = cpy.deepcopy(d3)

v[1] = 'Rafael'
v['d'][0] = 'Parente'

print(d3)
print(v)

