n = int(input ("Digite um número: "))

res = 1

for i in range(1, n + 1):
  res += 1 / i
  
print(f'Resultado: {res:.2f}')