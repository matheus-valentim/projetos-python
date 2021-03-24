def leiaint(num):
    valor = 0
    while True:
        if num.isnumeric():
            valor = int(num)
            break
        if num.isnumeric() is False:
            num = input('diga um numero: ')
    return valor


n = input('diga um numero: ')
print(f'o numero que voce digitou é: {leiaint(n)}')