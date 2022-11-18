ax = float(input('Coordenada X de A: '))
ay = float(input('Coordenada Y de A: '))

bx = float(input('Coordenada X do vetor B: '))
by = float(input('Coordenada Y do vetor B: '))

n = int(input('Quantidade : '))

for i in range(1, n + 1):
  print(f'P{i}: ({ax + bx}, {ay + by})')
  
  ax = ax + bx
  ay = ay + by