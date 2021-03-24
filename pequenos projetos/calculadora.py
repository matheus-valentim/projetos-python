from time import sleep
n1 = int(input('digite um numero:'))
n2 = int(input('digite outro numero: '))
n = 0

while n != 5:
    print('==============================')
    n = int(input('1- somar\n2- multiplicar\n3- maior valor\n4- novos numeros\n5- sair o programa\n'))

    if n == 1:
        print('a soma é: {}'.format(n1 + n2))

    elif n == 2:
        print(' a multiplicação é: {}'.format(n1 * n2))

    elif n == 3:
        if n1 > n2:
            print('o maior valor é {}'.format(n1))
        elif n2 > n1:
            print('o maior valor é {}'.format(n2))
        elif n1 == n2:
            print('o valores sao iguais')

    elif n == 4:
        n1 = int(input('digite um numero:'))
        n2 = int(input('digite outro numero: '))
    elif n == 5:
        print('...')
    else:
        print('opção invalida, tente novamente')
    sleep(1)
print('encerrando...')