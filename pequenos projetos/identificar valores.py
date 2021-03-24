lista = []
maior = menor = menorP = maiorP = 0
for n in (range(0, 5)):
    lista.append(int(input(f'diga um valor para a posição {n}:  ')))
    if n == 0:
        maior = menor = lista[n]
        menorP = maiorP = n
    else:
        if lista[n] > maior:
            maior = lista[n]
            maiorP = n

        elif lista[n] < menor:
            menor = lista[n]
            menorP = n

print(f'o maior valor é {maior} e ele esta na posição {maiorP}')
print(f'o menor valor é {menor} e esta na posição {menorP}')
