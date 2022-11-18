import math

print('Determine os coeficientes para a seguinte equação: equação Ax²+Bx+C=0')

a = float(input('Digite o coeficiente A: '))
b = float(input('Digite o coeficiente B: '))
c = float(input('Digite o coeficiente C: '))

# Ax² + Bx + C = 0

delta = b**2 - 4 * a * c
x1 = (-b + math.sqrt(delta)) / (2 * a)
x2 = (-b - math.sqrt(delta)) / (2 * a)

print(f'O valor de delta é: {delta}')
print(f'O valor de X\' é: {x1}')
print(f'O valor de X\'\' é: {x2}')