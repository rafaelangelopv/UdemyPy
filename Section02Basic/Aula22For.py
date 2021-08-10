"""

For in
em Python

Iterando strings com for
Função range (start=0, stop, step=1)

"""
# 1
texto = 'Python'
c = 0
while c < len(texto):
    print(texto[c])
    c += 1
# 2
texto = 'Python'
for letra in texto:
    print(letra)

# 3
for n in range(0, 10, 1):  # start=0, stop=10, step=1
    print(n)

# 4
for n in range(20, 9, -1):  # start=20, stop=9, step=-1
    print(n)

# 5

for n in range(0, 100, 8):
    print(n)

print('#'*10)  # separa as duas formas

for n in range(100):
    if n % 8 == 0:
        print(n)


# 6

texto = 'Python'
nova_string = ''

# continue - pula para o proximo laço
# break - termina o laço

for letra in texto:
    if letra == 't':
        continue  # pula o 't'
        nova_string = nova_string + letra.upper()
    elif letra == 'h':
        nova_string += letra.upper()
        break  # termina no H
    else:
        nova_string += letra
print(nova_string)
