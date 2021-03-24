c = s = 0
while True:
    n = int(input('diga um número para somar(pare com 999): '))
    if n == 999:
        break
    s += n
    c += 1
print(f'a soma dos {c} valores foi {s}')
