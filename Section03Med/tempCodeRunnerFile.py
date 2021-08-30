def funcao1(funcao2, *args, **kwargs):
    # recebe a funcao2 e todos os argumentos restantes
    return funcao2(*args, **kwargs)
    # retorna a funcao2 e todos os argumentos restantes


def fala(nome):
    return f'Oi {nome}'


def saudacao(nome, saudacao):
    return f'{saudacao} {nome}'


exec1 = funcao1(fala, 'Rafael')
exec2 = funcao1(saudacao, 'Rafael', saudacao='Bom dia!')
print(exec1)
print(exec2)