x = float(input('X: '))
y = float(input('Y: '))

if x >= 0 and y >= 0:
    print('Primeiro quadrante')
elif x < 0 and y < 0:
    print('Segundo quadrante')
elif x < 0 and y < 0:
    print('Terceiro quadrante')
else:
    print('Quarto quadrante')
