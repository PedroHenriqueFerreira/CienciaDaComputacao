from random import randint

cartas = []
tipos = ['Ás', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
naipes = ['paus', 'ouros', 'copas', 'espadas']

for naipe in naipes:
    for tipo in tipos:
        cartas.append(f'{tipo} de {naipe}')
        
for i in range(4):
    print(f'Jogador {i + 1}: ', end='')
    for _ in range(5):
        carta = cartas[randint(0, len(cartas) - 1)]
        print(carta, end=' | ')
        cartas.remove(carta)
    print('')