"""

While / Iteract [passar por cada um dos elementos]

"""
#         Índices
#         0123456789.........................33

frase = 'o rato roeu a ropa do rei de roma'
tamanho_frase = len(frase)
# print(tamanho_frase)
contador = 0
# print(frase[5])
nova_string = ''

# 1
while contador < 10:
    print(contador)
    contador += 1

# 2
while contador < tamanho_frase:
    print(frase[contador], contador)
    contador += 1

# 3
while contador < tamanho_frase:
    nova_string += frase[contador]
    print(nova_string)
    contador += 1

# 4
frase = 'o rato roeu a ropa do rei de roma'
tamanho_frase = len(frase)
contador = 0
nova_string = ''

input_do_usuario = input('Qual letra deseja colocar maiúscula: ')

# Iteract

while contador < tamanho_frase:
    letra = frase[contador]
    if letra == input_do_usuario:
        nova_string += input_do_usuario.upper()
    else:
        nova_string += letra
    contador += 1
print(nova_string)
