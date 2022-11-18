n = int(input('Digite um número: '))
if n % 2 == 0: n -= 1
else: n -= 2

tot = 0


for i in range(n, 0, -2):
  tot += i
  
print(tot)