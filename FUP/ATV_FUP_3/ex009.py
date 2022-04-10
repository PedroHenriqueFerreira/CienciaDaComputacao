n = int(input('Digite um número: '))

print(f'Divisores de {n}: ', end='')
for i in range(n, 0, -1):
  if n % i == 0: 
    if i != 1:
      print(i, end=', ')
    else:
      print(f'e {i}')