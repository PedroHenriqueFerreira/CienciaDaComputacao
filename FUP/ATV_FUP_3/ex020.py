n = str(input("Digite um número binário: "))
res = 0
exp = 0

for i in range(len(n) - 1, -1, -1):
  res += int(n[i]) * 2**exp
  exp += 1

print(res)