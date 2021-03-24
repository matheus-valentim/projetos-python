s = 0
n = int(input('digite um numero: '))
for c in range(1, n+1):
    if n % c == 0:
        print('\033[34m', end=' ')
        s += 1
    else:
        print('\033[31m', end=' ')
    print(c)
print('\033[mo numero {} foi divisivel {} vezes'.format(n, s))
if s == 2:
    print('por isso ele é primo!')
else:
    print('por isso ele nao é primo')