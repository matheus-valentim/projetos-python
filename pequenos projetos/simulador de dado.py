def rolar(num):
    from random import randint
    from time import sleep
    print('-' * 30)
    print('ele esta rolando...')
    sleep(0.5)
    a = randint(1, num)
    print(a)
    print('-' * 30)


rolar(int(input('qual o numero de lados do dado? ')))
while True:
    escolha = input('voce quer continuar? ').strip().lower()
    if escolha[0] == 's':
        rolar(int(input('qual o numero de lados do dado? ')))
    elif escolha[0] == 'n':
        print('que os dados te guiem!!')
        break
    else:
        escolha = input('voce quer continuar? ').strip().lower()