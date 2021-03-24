from random import choice
e = input('escolha um \nA)pedra \nB)papel \nC)tesoura \nqual a sua escolha? ').strip().upper()
p = 'pedra'
pa = 'papel'
t = 'tesoura'
L = [p, pa, t]
c = choice(L)
if e == 'A':
    print('voce escolheu pedra')
    if c == 'pedra':
        print('voces empataram!!')
    elif c == 'papel':
        print('voce perdeu!')
    elif c == 'tesoura':
        print('voce ganhou!!')
    
elif e == 'B':
    print('voce escolheu papel')
    if c == 'pedra':
        print('voce ganhou!!')
    elif c == 'papel':
        print('empate')
    elif c == 'tesoura':
        print('voce perdeu')

elif e == 'C':
    print('voce escolheu tesoura')
    if c == 'pedra':
        print('voce perdeu')
    elif c == 'papel':
        print('voce ganhou!!')
    elif c == 'tesoura':
        print('empate!')

else:
    print('voce digitou errado, tente de novo')
