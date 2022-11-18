n = int(input ("Digite um número: "))

count = 1
for i in range(1, n + 1):
  for _ in range(i):
    print(f'0{count}' if count < 10 else count, end='  ')
    count += 1
  print()