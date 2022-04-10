n = int(input ("Quantidade de pontos: "))
xmin = xmax = ymin = ymax = 0

for i in range(1, n + 1):
  x = float(input(f'Digite a {i}° coordenada X: '))
  y = float(input(f'Digite a {i}° coordenada Y: '))
  
  if i == 1: 
    xmin = xmax = x
    ymin = ymax = y
  else:  
    if x > xmax: xmax = x
    elif x < xmin: xmin = x
    
    if y > ymax: ymax = y
    elif y < ymin: ymin = y

print(f'Min: ({xmin}, {ymin})')
print(f'Max: ({xmax}, {ymax})')