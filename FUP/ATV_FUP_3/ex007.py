n = int(input('Digite um número: '))
res = 1

for i in range(n, 0, -1):
  res *= i

print(res)