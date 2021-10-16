"""
* Criar variáveis para nome (str), idade (int),
* altura (float) e peso (float) de uma pessoa
* Criar variável com o ano atual (int)
* Obter o ano de nascimento da pessoa (baseado na idade e no ano atual)
* Obter o IMC da pessoa com 2 casas decimais (poeso e na altura da pessoa)
* Exibir um testo com todos os valores na tela usando F-Strings (com as chaves)

"""
# Variáveis
nome = 'Rafael Angelo'
idade = 30
altura = 1.68
peso = 98.2
ano_atual = 2021

# Cálculos
nascimento = ano_atual - idade
imc = peso / altura**2

# Texto
print(f'{nome} tem {idade} anos de idade, {altura} de altura e pesa {peso}.')
# .2f, duas casas decimais no número float
print(f'O imc de {nome} é {imc:.2f}')
print(f'{nome} nasceu em {nascimento}')
