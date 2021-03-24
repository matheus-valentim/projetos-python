a = int(input('qual o primeiro lado? '))
b = int(input('qual o segundo? '))
c = int(input('e o terceiro? '))
if abs(b - c) < a < b + c and abs(a - c) < b < a + c and abs(b - a) < c < c + a:
    print('voce pode formar um triangulo!!')
    if a != b != c != a:
        print('o triangulo é escaleno!')
    if a == b == c:
        print('esse triangulo é equilatero!')
    if a == b != c or c == b != a or a == c != b:
        print('esse triangulo é isosceles!')
else:
    print('voce nao pode formar um triangulo')
