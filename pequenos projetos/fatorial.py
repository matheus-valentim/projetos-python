n = int(input('me diga um numero: '))
f = n
m = 1
while f > 0:
    print(f,end=' ')
    print(' x 'if f > 1 else ' = ',end='')
    m *= f
    f = f - 1

print(m)
