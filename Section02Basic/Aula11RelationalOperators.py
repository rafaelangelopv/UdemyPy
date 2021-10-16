"""

Operadores Relacionais

== , igualdade 
>  , maior que
>= , maior que ou igual a
<  , menor que
<= , menor que ou igual a
!= , diferença

"""

##-----------------------------------==-----------------------------------##

print(2 == 2)  # Pergunta se 2 é igual a 2. Responde valor bool
print(2 == 1)  # Pergunta se 2 é igual a 2. Responde valor bool


num_1 = 2  # int
num_2 = '2'  # str

print(num_1, num_2)  # Mostra 2 2, int e str
print(num_1 == num_2)  # False, int diferente de str


num_1 = 2  # int
num_2 = 2  # int

expressao = (num_1 == num_2)

print(expressao)

##----------------------------------->-----------------------------------##

num_1 = 3  # int
num_2 = 2  # int

expressao = (num_1 > num_2)

print(expressao)

##----------------------------------->=-----------------------------------##

num_1 = 3  # int
num_2 = 2  # int

expressao = (num_1 >= num_2)

print(expressao)

##-----------------------------------<=-----------------------------------##

num_1 = 3  # int
num_2 = 2  # int

expressao = (num_1 <= num_2)

print(expressao)

##-----------------------------------!=-----------------------------------##

var_1 = 'Rafael'
var_2 = 'Angelo'

expressao = (var_1 != var_2)

print(expressao)

##-----------------------------------Exemplo / Aplicação-----------------------------------##

nome = input('Qual o seu nome? ')
idade = input('Qual a sua idade? ')

idade = int(idade)

# Limite paar pegar empréstimo
idade_limite = 18
idade_menor = 20  # Muito Jovem
idade_maior = 30  # Passou da idade

# Aplicando com idade limite
if idade >= idade_limite:
    print(f'{nome} pode pegar o empréstimo. 1')
else:
    print(f'{nome} Não pode pegar o empréstimo. 1')

# Aplicando com meno e maior idade
if idade >= idade_menor and idade <= idade_maior:
    print(f'{nome} pode pegar o empréstimo. 2')
else:
    print(f'{nome} Não pode pegar o empréstimo. 2')
