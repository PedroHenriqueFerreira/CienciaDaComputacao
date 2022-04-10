n1 = int(input('Digite um número: '))
n2 = int(input('Digite mais um número: '))

max = n1 if n1 > n2 else n2
min = n2 if n1 > n2 else n1

rest = 0

while min != 0:
  rest = max % min
  max = min
  min = rest
  
print(f'MDC: {max}')