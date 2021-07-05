"""

Operadores Lógicos

and     , 
or      ,
not     ,
in      ,
not in  ,


"""

##-----------------------------------and-----------------------------------##

# (Verdadeiro E Verdadeiro) = True
# (Verdadeiro E Falso) = False
# O AND retorna True se as duas condições forem atendidas
comparacao1 and comparacao2

##-----------------------------------or-----------------------------------##

# O OR retorna TRUE se pelo menos uma comparação for verdadeira
# (Verdadeiro E Falso) = True

comp1_OR_comp2

##-----------------------------------not-----------------------------------##

a = 2
b = 3

if not b > a:
    print('B é maior do que A')
else:
    print('A é maior do que B.')


a = ''
b = 0

if not a:  # Para verificar se o valor está vazio
    print('Por favor, preencha o valor de A.')

    # O valor de B está igual a zero e também é considerado False ou vazio.
    # Caso tenha algo dentro de A, vai retornar um conteúdo vazio.

##-----------------------------------in // not in-----------------------------------##

nome = 'Rafael Angelo'

if 'Raf' in nome:
    print('Existe.')
else:
    print('Não existe.')

if 'Vale' not in nome:
    print('Executei.')
else:
    print('Existe o texto.')

##-----------------------------------Exemplo Aplicação -----------------------------------##

usuario = input('Username: ')
senha = input('Password: ')

usuario_bd = 'rafaelangelopv'
senha_bd = '123456'

if usuario_bd == usuario and senha_bd == senha:
    print('Você está logado no Sistema')
else:
    print('Usuário ou Senha inválidos')
