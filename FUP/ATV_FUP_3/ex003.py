max = 0

for i in range(10):
  n = int(input ("Digite um número: "))
  
  if max < n or i == 0: max = n
  
print(f'Valor maior: {max}')