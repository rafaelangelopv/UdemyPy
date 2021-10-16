"""

Len - Quantidade de caracteres

"""

##-----------------------------------Uso inicial-----------------------------------##

usuario = input('Digite seu usuário: ')
qtd_caracteres = len(usuario)

print(usuario, qtd_caracteres, type(qtd_caracteres))

if qtd_caracteres < 6:
    print('Você precisa digitar pelo menos 6 caracteres')
else:
    print("Você foi cadastrado no sistema.")

##-----------------------------------Teste 01-----------------------------------##

string1 = input('Digite alguma coisa: ')
string2 = input('Digite outra coisa: ')

print(
    f'A quantidade total de caracteres digitados foi de {len(string1) + len(string2)}')

##-----------------------------------Função __len__ -----------------------------------##

print(string2.__len__())  # Função chamada com ponto, __len__

# Não funciona com números

print(len(12345))  # Dá erro: 'has no len'
