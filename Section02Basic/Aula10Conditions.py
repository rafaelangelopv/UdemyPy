"""

Condições IF, ELIF e ELSE // SE, SenãoSe, Senão

"""

##-----------------------------------if-----------------------------------##

if True:
    print("Verdadeiro")

    num_1 = 2
    num_2 = 4

    print(num_1 + num_2)

##-----------------------------------if / elif / else-----------------------------------##

if True:
    print('Verdadeiro')
    print('teste teste2')

elif True:
    print('Agora é verdadeiro')
    nome = input("Qual o seu nome? ")

    print(f'Seu nome é {nome}.')

elif False:
    print('Mais uma verdadeira')
    print(22+22)

else:
    print("Não é verdadeiro")
    print("Olá")

print('A minha expressão não é verdadeira')

# O código procura o primeiro que for verdadeiro e executa, mesmo que o proximo seja verdadeiro não será executado.
# SE:
# SENÃOSE:
# SENÃO:
