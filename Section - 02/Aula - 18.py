"""

Manipulando strings

* String indices
* Fatiamento de strings [inicio:fim:passo]
* Funções built-in len, abs, type, print, etc...

Essas funções podem ser usadas diretamente em cada tipo.

Você pode conferir tudo isso em:

https://docs.python.org/3/library/functions.html (tipos built-in)
https://docs.python.org/3/library/stdtypes.html (funções built-in)


"""
# Positivos [012345678]
texto = 'Python s2'

print(texto[2])  # t
print(texto[8])  # 2
print(texto[6])  # ""
print(texto[9])  # "Erro - Fora do Range"

# Negativos -[987654321]
texto = 'Python s2'

# retira a barra no final da URL. Antes dos dois pontos, sem numerar, indica que começa a contagem do início
url = 'www.google.com.br/'
# thon, strings da posicao 2o até o 5o. Como o ultimo nao é incluido, deve colocar até 6
print(url[:-1])
nova_string = texto[2:6]
print(nova_string)

# Positivos
texto = 'Python s2'
nova_string = texto[:]  # Python s2, do início ao fim
print(nova_string)
nova_string = texto[:6]  # Python, do início ao 5o
print(nova_string)
nova_string = texto[7:]  # s2, do 's' ao fim
print(nova_string)

# Negativos
texto = 'Python_s2'
nova_string = texto[-1]  # 2, ultimo
print(nova_string)
nova_string = texto[-9]  # P, primeiro
print(nova_string)
nova_string = texto[-9:-3]  # Python
print(nova_string)
nova_string = texto[:-1]  # Python_s
print(nova_string)
nova_string = texto[:-2]  # Python_
print(nova_string)

# Intercalado
texto = 'Python_s2'
nova_string = texto[0:6:2]  # Pto
print(nova_string)
nova_string = texto[0::3]  # Ph
print(nova_string)

# Len - Quantidade de caracteres
texto = 'Python_s2'
print(len(texto))  # 9, quantidade de strings
for letra in texto:
    print(letra)
