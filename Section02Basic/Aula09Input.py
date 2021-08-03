"""
Entrada de dados

Exemplos:
  Idade
  Calculadora de Soma

"""
##-----------------------------------Idade-----------------------------------##
nome = input("Qual o seu nome? ")
idade = input("Qual a sua idade? ")
ano = 2021
ano_nascimento = ano - int(idade)  # transformado de str para int

print()
print(f'O usuário digitou {nome} e o tipo da variável é '
      f'{type(nome)}.')
print()
print(f'{nome} tem {idade} anos, {nome} nasceu no ano de {ano_nascimento}.')
print()
# O valor digitado em input sempre vai retornar uma string

##-----------------------------------Calculadora de Soma-----------------------------------##

numero_1 = int(input('Digite um número: '))
# alterou str to int
numero_2 = input('Digite outro número: ')
numero_2 = int(numero_2)
# alterou str to int

print(numero_1 + numero_2)
print(numero_1 ** numero_2)
