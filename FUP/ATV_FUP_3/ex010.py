n1 = int(input('Digite um número: '))
n2 = int(input('Digite mais um número: '))

i = 2
mmc = 1

while True:
  if n1 % i == 0 or n2 % i == 0:
    print(f'{n1}, {n2} | {i}')
    mmc *= i
    if n1 % i == 0: n1 //= i  
    if n2 % i == 0: n2 //= i
  else:
    i += 1
  
  if n1 == 1 and n2 == 1:
    print(f'{n1}, {n2} | -')
    break

print(f'MMC: {mmc}')