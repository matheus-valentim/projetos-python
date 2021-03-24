nome = input('me diga seu nome completo: ').strip().title()
nomeCortado = nome.split()
print(f'seu primeiro nome é: {nomeCortado[0]}')
print(f'seu ultimo nome é: {nomeCortado[-1]}')
