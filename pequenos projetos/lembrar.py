produtos = ('maça', 5,
            'banana', 3,
            'couve', 0.5,
            'limão', 3,
            'laranja', 6,
            'morango', 7)
print('=' * 30)
print(f'{"LISTA DE PRODUTOS":^30}')
print('='*30)
for pos in range(0, len(produtos)):
    if pos % 2 == 0:
        print(f'{produtos[pos]:.<30}', end='')
    else:
        print(f'R${produtos[pos]:>5.2f}')