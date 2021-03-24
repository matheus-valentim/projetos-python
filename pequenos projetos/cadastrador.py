pessoas = {}
lista = []
contador = 0
media = soma= 0

while True:
    pessoas.clear()
    print('=' * 30)
    contador += 1
    pessoas['nome'] = input('nome: ').strip()
    pessoas['idade'] = int(input('idade: '))
    soma += pessoas['idade']

    pessoas['sexo'] = input('sexo (M/F): ').strip().lower()[0]
    while pessoas['sexo'] not in 'mf':
        pessoas['sexo'] = input('sexo (M/F): ').strip().lower()[0]
    escolha = ' '

    lista.append(pessoas.copy())
    while escolha not in 'sn':
        escolha = input('voce quer cadastrar mais gente? [S/N] ')
    if escolha in 'n':
        break

print('=' * 30)
media = soma / len(lista)
print(lista)
print(f'ao todo temos {len(lista)} pessoas cadastradas')
print(f'a média de idade é: {media}')
print('as mulheres são: ', end=' ')

for m in lista:
    if m['sexo'] in 'f':
        print(m['nome'], end=' ')

print('\nas pessoas com idade acima da média são: ', end=' ')

for i in lista:
    if i['idade'] >= media:
        print(i['nome'])
