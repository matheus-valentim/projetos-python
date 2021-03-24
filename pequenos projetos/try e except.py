def leiaint(num):
    valor = 0
    while True:
        try:
            valor = int(num)
            break
        except (ValueError, TypeError):
            print('erro, digite um valor valido!')
            num = input('diga um valor inteiro: ')
    return valor


def leiafloat(num):
    valor = 0
    while True:
        try:
            valor = float(num)
            break
        except(ValueError, TypeError):
            num = input('diga um valor real: ')
    return valor


n = leiaint(input('diga um valor inteiro: '))
n2 = leiafloat(input('digie um valor real: '))

print(f'o numero inteiro é: {n}')
print(f'o numero real é: {n2}')