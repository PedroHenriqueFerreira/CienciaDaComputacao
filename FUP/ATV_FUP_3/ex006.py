soma = 0
max = 0
n = 0

while n >= 0:
  n = int(input ("Digite um número: "))
  
  if max < n: max = n
  soma += n
print(f'Soma: {soma}')
print(f'Maior: {max}')