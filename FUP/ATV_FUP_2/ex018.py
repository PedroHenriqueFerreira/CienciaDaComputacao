ax = float(input('Coordenada x de A: '))
ay = float(input('Coordenada y de A: '))
bx = float(input('Coordenada x de B: '))
by = float(input('Coordenada y de B: '))
cx = float(input('Coordenada x de C: '))
cy = float(input('Coordenada y de C: '))

if ax < bx and ay < by:
    if (ax <= cx <= bx and ay <= cy <= by):
        print('C está contido')
    else:
        print('C não está contido')
else:
    print('Retângulo inválido')
