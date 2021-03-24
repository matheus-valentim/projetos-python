from random import randint


def sorteia(lista):
    for c in range(0, 5):
        lista.append(randint(0, 10))


def somapar(lista):
    s = 0
    for v in lista:
        if v % 2 == 0:
            s += v
    print(s)



numeros = []
sorteia(numeros)
print(f'os numeros são: {numeros}')
print(f'somando os valores pares fica: ', end='')
somapar(numeros)
