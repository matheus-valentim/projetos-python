from random import randint
n = int(input('advinhe um numero entre 0 e 10!! '))
a = randint(0, 10)
t = 1
while not a == n:
    if a > n:
        n = int(input('mais...tente de novo: '))
        t += 1
    if a < n:
        n = int(input('menor...tente de novo: '))
        t += 1
    if a == n:
        print('voce acertou o numero com {} tentativas!'.format(t))

