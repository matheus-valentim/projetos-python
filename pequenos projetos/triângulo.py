a = int(input('primeiro segmento: '))
b = int(input('segundo segmento: '))
c = int(input('terceiro segmento: '))
if abs(b - c) < a < b + c and abs(a - c) < b < a + c and abs(a - b) < c < a + b:
    print('com essas medidas pode se formar um triangulo!')
else:
    print('com essas medidas nao pode formar um triangulo :(')
