n = int(input("Altura da pirâmide: "))
res = 0

for i in range(1, n + 1):
  res += i ** 2

print(f'Blocos utilizados: {res}')