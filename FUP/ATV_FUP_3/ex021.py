x = int(input('Coordenada X inicial: '))
y = int(input('Coordenada Y inicial: '))

print('Coordenadas possíveis: ')
coord = ''

for i in range(1, 9):
  if(y != i):
    coord += f'({x},{i}),'
    
  if(x != i):
    coord += f'({i},{y}),'
    
print(coord.rpartition(',')[0])