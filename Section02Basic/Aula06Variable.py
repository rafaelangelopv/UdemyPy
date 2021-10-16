"""
Variáveis

Iniciar com letra
Pode conter números
Separar _
letras minúsculas

"""
# nome = 'Rafael'
# print(nome, type(nome))

nome = 'Rafael Angelo'
idade = 30              # int
altura = 1.68           # float
e_maior = idade > 18    # bool
data_1 = True           # bool explicit first letter uppercase
data_atual = 2021       # int
peso = 98
imc = peso / (altura**2)

print('Nome:', nome)
print('Idade:', idade)
print('Altura:', altura)
print('Peso:', peso)
print('É maior de idade:', e_maior)

print(idade * altura)
print(nome, 'tem', idade, 'anos de idadade e seu imc é', imc)
