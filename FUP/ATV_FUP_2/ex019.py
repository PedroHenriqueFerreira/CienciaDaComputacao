ax = float(input('Coordenada x de A: '))
ay = float(input('Coordenada y de A: '))
bx = float(input('Coordenada x de B: '))
by = float(input('Coordenada y de B: '))
cx = float(input('Coordenada x de C: '))
cy = float(input('Coordenada y de C: '))

xmin = 0
xmax = 0
if bx <= ax >= cx:
    xmax = ax
    if bx >= cx:
        xmin = cx
    else:
        xmin = bx
elif ax <= bx >= cx:
    xmax = bx
    if ax >= cx:
        xmin = cx
    else:
        xmin = ax
else:
    xmax = cx
    if bx >= ax:
        xmin = ax
    else:
        xmin = bx
        
ymin = 0
ymax = 0
if by <= ay >= cy:
    ymax = ay
    if by >= cy:
        ymin = cy
    else:
        ymin = by
elif ay <= by >= cy:
    ymax = by
    if ay >= cy:
        ymin = cy
    else:
        ymin = ay
else:
    ymax = cy
    if by >= ay:
        ymin = ay
    else:
        ymin = by
        
print(f'Largura: {xmax - xmin} e Altura: {ymax - ymin}')
