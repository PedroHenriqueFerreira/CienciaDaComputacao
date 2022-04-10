print('Determine os coeficientes e o valor de X para a seguinte função: f(x)=Ax²+Bx+C')

a = float(input('Digite o coeficiente A: '))
b = float(input('Digite o coeficiente B: '))
c = float(input('Digite o coeficiente C: '))

x = float(input('Digite o valor de X: '))

res = a * x**2 + b * x + c
print(f'O resultado é {res}')