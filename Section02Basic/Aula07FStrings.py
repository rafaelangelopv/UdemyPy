
# F strings


nome = 'Rafael Angelo'
idade = 30              # int
altura = 1.68           # float
e_maior = idade > 18    # bool
data_1 = True           # bool explicit first letter uppercase
data_atual = 2021       # int
peso = 98
imc = peso / (altura**2)

# Escrita direta
print(nome, 'tem', idade, 'anos de idadade e seu imc é', imc)

# Usando F strings
print(f'{nome} tem {idade} anos de idadade e seu imc é {imc}')

# Usando F strings // .2 são duas casas decimais e o f é float
print(f'{nome} tem {idade} anos de idadade e seu imc é {imc:.2f}')

# Usando Format
print('{} tem {} anos e seu imc é {:.2f}'.format(nome, idade, imc))

# Usando Format // numerando as chaves, pode mudar a ordem
print('{0} tem {1} anos e seu imc é {2}'.format(nome, idade, imc))

# Usando Format // numerando as chaves
print('{n} tem {i} anos e seu imc é {im}'.format(n=nome, i=idade, im=imc))
