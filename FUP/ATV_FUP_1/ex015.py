import math


xa = float(input('Digite o ponto X da coordenada A: '))
ya = float(input('Digite o ponto Y da coordenada A: '))
xb = float(input('Digite o ponto X da coordenada B: '))
yb = float(input('Digite o ponto Y da coordenada B: '))

x = xb - xa
y = yb - ya

print(f'A distância entre ({xa}, {ya}) e ({xb}, {yb}) é: {math.sqrt(y**2 + x**2)}')