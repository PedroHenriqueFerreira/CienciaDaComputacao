ax = float(input('Coordenada X de A: '))
ay = float(input('Coordenada Y de A: '))

bx = float(input('Coordenada X do vetor B: '))
by = float(input('Coordenada Y do vetor B: '))

xmin = float(input('Min X da caixa: '))
ymin = float(input('Min Y da caixa: '))

xmax = float(input('Max X da caixa: '))
ymax = float(input('Max Y da caixa: '))

i = 1

colide = False

while ax < xmax:
  if xmax > ax > xmin and ymax > ay > ymin:
    colide = True
    break
  
  ax = ax + bx
  ay = ay + by
  
  i += 1
  
if colide: print('A reta cruza a caixa')
else: print('A reta não cruza a caixa')