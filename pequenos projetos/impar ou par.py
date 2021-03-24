from random import randint
c = 0
while True:
    print("diga um numero para somar com a escolha do computador e advinha se é ímpar ou par!")
    n = int(input('qual numero?'))
    numPC = randint(1, 10)
    soma = n + numPC
    e = ' '
    while e not in 'pi':
        e = str(input('par ou impar? ')).strip().lower()[0]
    if e == 'p':
        if soma % 2 == 0:
            print('voce venceu!!!!')
            c += 1
        else:
            print('voce perdeu')
            break
    if e == 'i':
        if soma % 2 == 0:
            print('voce venceu!!')
            c += 1
        else:
            print('voce perdeu')
            break
print(f'GAME OVER! voce venceu {c} vezes')
