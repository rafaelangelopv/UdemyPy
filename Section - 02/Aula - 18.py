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

url = 'www.google.com.br/'
print(url[:-1])  # retira a barra no final da URL
