from random import randint

def explicacao():
    print('-' * 60)
    print('             bem vindo ao jogo de advinhaçôes!')
    print('-' * 60)
    print('voce vai comecar com 15 pontos e perder um a cada erro.')
    print('um número aleatório entre 1 e 15 vai ser sorteado, boa sorte!')
    print('-' * 60)


explicacao()
pontos = 15
escolhamaquina = randint(1, 15)

while True:
    escolhajogador = int(input('advinhe o numero: '))
    if escolhajogador == escolhamaquina:
        print(f'voce venceu e com {pontos} pontos!')

        break
    elif escolhajogador < escolhamaquina:
        print('é  maior!')
        pontos -= 1
    elif escolhajogador > escolhamaquina:
        print('é menor!')
        pontos -= 1