from random import choice


def menu():
    print('-' * 35)
    print('vamos bricar de jogo da forca!!')
    print('voce tem 7 chances e a contagem da palavra começa no 0. EX: bacon (no B a posição é 0 e no N 4)')
    print('escolha o modo:\nfrutas: 0\npais: 1\nobjetos: 2\nnomes: 3\ntodos acima: 4')
    print('-' * 35)


def confirmacao(modo):
    if modo == 0:
        escolha = choice(lista[0])
        return escolha
    if modo == 1:
        escolha = choice(lista[1])
        return escolha
    if modo == 2:
        escolha = choice(lista[2])
        return escolha
    if modo == 3:
        escolha = choice(lista[3])
        return escolha
    if modo == 4:
        escolha = choice(lista)
        escolhageral = choice(escolha)
        return escolhageral


def escolhajogador(letra):
    pos = 0
    while True:
        if len(letra) > 1:
            print('como apenas uma letra não foi digitada essa tentativa é falha.')
            break
        if letra != maquina[pos]:
            pos += 1
        elif letra == maquina[pos]:
            print(f'voce encontrou a letra na posição {pos}')
            pos += 1
            while True:
                if pos >= len(maquina):
                    break
                if letra == maquina[pos]:
                    print(f'voce tambem encontrou a letra na posição {pos}!')
                    pos += 1
                elif letra != maquina[pos]:
                    pos += 1
            print('-' * 35)
            break
        if pos >= len(maquina):
            print('a letra n existe!')
            print('-' * 35)
            break



# programa principal
# aqui ficam as listas
lista = []
frutas = ['maça', 'banana', 'melancia', 'melao', 'uva', 'pera',
          'caqui', 'abacate', 'abacaxi', 'açai', 'acerola', 'caja']
pais = ['brasil', 'alemanha', 'inglaterra', 'peru', 'argentina', 'frança', 'japao',
        'china', 'tailandia', 'uruguay', 'venezuela', 'portugal', 'espanha']
objetos = ['lapis', 'folha', 'sofa', 'balde', 'autralia', 'cuba']
nomes = ['matheus', 'camila', 'sophia', 'marcos', 'marcelo', 'gabriela', 'tiago', 'alana',
         'alex', 'jonas', 'ana', 'julia', 'carolina', 'lucas']

# aqui dou append e apago
lista.append(frutas[:])
lista.append(pais[:])
lista.append(objetos[:])
lista.append(nomes[:])
del frutas
del pais
del objetos
del nomes

menu()
num = int(input('diga um numero correspondente ao menu:'))

while not 0 <= num <= 4:
    num = int(input('diga um numero correspondente ao menu:'))
maquina = confirmacao(num)

pontos = 7
while pontos > 0:
    print(f'voce tem {pontos} tentativas')
    pontos -= 1
    jogador = input('fale uma letra: ').strip()
    escolhajogador(jogador)

print('-' * 35)
print(f'a palavra possui {len(maquina)} letras')
opcao = input('qual palavra voce acha que é a certa? ')
if opcao == maquina:
    print(f'parabens!!! voce acertou!! a palavra é {maquina}')
elif opcao != maquina:
    print(f'infelizmente voce errou, a palavra era {maquina}')
