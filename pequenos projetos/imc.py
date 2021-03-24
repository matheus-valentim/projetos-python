peso = float(input('me diga seu peso em kg: '))
altura = float(input('me diga sua altura em metros: '))
imc = peso / (altura ** 2)
if imc <= 18.5:
    print('voce esta abaixo do peso')
elif 18.5 < imc <= 25:
    print('seu peso é ideal')
elif 25 < imc <= 30:
    print('voce esta acima do peso')
elif 30 < imc <= 40:
    print('voce esta obeso')
else:
    print('obesidade morbida')
