PI = 3.14
h = float(input('Digite a altura do cilindro: '))
r = float(input('Digite o raio da base do cilindro: '))

base = PI * r**2

print(f'A área lateral do cilindro é: %.4f'%(2*PI*r*h))
print(f'A área da base do cilindro é: %.4f'%(base))
print(f'O volume do cilindro é: %.4f'%(base * h))