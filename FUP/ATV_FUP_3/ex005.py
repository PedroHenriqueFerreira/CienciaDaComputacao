qtd = int(input('Quantidade de números: '))
soma = 0
max = 0

for i in range(qtd):
  n = int(input ("Digite um número: "))
  
  if max < n or i == 0: max = n
  soma += n
print(f'Soma: {soma}')
print(f'Maior: {max}')