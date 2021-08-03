"""
Exercícios usando: Lógica, if, elif, else, .isgit
"""


"""
Faça um programa que peça ao usuário para digitar um número inteiro, informe se este número é par ou ímpar.
Caso o usuário não digite um número inteiro, informe que não é um numero inteiro.
"""
##----------------------------resposta-----------------------##

numero_inteiro = input('Digite um número inteiro: ')

if numero_inteiro.isdigit():

    numero_inteiro = int(numero_inteiro)

    if numero_inteiro % 2 == 0:
        print(f'Você digitou {numero_inteiro}. Este número é par!')
    else:
        print(f'Você digitou {numero_inteiro}. Este número é ímpar!')

else:
    print(f'Você digitou {numero_inteiro}, Não é um número inteiro.')

##----------------------------invertido-----------------------##

numero_inteiro = input('Digite um número inteiro: ')

if not numero_inteiro.isdigit():

    print(f'Você digitou {numero_inteiro}, Não é um número inteiro.')

else:
    numero_inteiro = int(numero_inteiro)

    if not numero_inteiro % 2 == 0:
        print(f'Você digitou {numero_inteiro}. Este número é ímpar!')
    else:
        print(f'Você digitou {numero_inteiro}. Este número é par!')


"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário descrito, exiba a saudação apropriada.

Ex.: Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

hora = input(
    'Por gentileza, digite o horário atual? [ Entre 0h e 23h (HH.MM) ]: ')

if hora.isdigit():

    hora = int(hora)

    if hora >= 0 and hora <= 11:
        print(f'\nHora atual: {hora}h da manhã!\nBom dia!')
    elif hora >= 12 and hora <= 17:
        print(f'\nHora atual: {hora}h\nBoa tarde!!')
    elif hora >= 18 and hora <= 23:
        print(f'\nHora atual: {hora}h\nBoa noite!!')
    else:
        print(f'\nO Horário digitado não está no intervalo entre 0h e 23h.\n')

else:
    print('\nHorário Inválido.\n')


"""
Faça um programa que peça o primeiro nome do usuário.
Se o nome tiver 4 letras ou menos escreva "Seu nome é curto";
Se tiver entre 5 e 6 letras, escreva "Seu nome é normal";
Maior que 6 escreva "Seu nome é muito grande".
"""

##----------------------------resposta-----------------------##

primeiro_nome = input('Digite o seu primeiro nome: ')
er = 'ERROR'

if primeiro_nome.isalpha():

    tamanho = len(primeiro_nome)

    if tamanho <= 4:
        print('Seu nome é curto! Possui até 4 letras!')
    elif tamanho >= 5 and tamanho <= 6:
        print('Seu nome é normal! Está entre a média...5 a 6 letras!')
    elif tamanho > 6 and tamanho <= 10:
        print('Seu nome é muito grande! Tem mais de 6 letras...')
    else:
        print(
            'Você ultrapassou o limite de 10 letras para o primeiro nome!')

else:
    print(
        f'\n\n{er:-^50}\n\nNão digite espaços, números ou caracteres especiais!\n\n')
