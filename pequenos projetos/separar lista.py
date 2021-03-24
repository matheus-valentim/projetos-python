lista = [[], []]
for elemento in range(1, 8):
    n = int(input('digite um valor: '))
    if n % 2 == 0:
        lista[0].append(n)
    elif n % 2 == 1:
        lista[1]. append(n)
lista[0].sort()
lista[1].sort()
print(f'a lista par é : {lista[0]}')
print(f'a lista impar é {lista[1]}')