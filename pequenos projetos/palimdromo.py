frase = str(input('diga uma frase:')).strip().upper()
sep = frase.split()
junto = ''.join(sep)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print('isso é um palindromo!!')
else:
    print('isso nao é um palindromo')
