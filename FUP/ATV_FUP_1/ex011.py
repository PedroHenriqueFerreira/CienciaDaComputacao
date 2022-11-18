import math


c1 = float(input('Digite o primeiro cateto do triângulo: '))
c2 = float(input('Digite o segundo cateto do triângulo: '))

h = math.sqrt(c1**2 + c2**2)

print(f'A hipotenusa vale: {h}')