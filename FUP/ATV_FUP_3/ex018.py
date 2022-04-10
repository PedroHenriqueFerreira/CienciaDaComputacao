n = int(input ("Número de parcelas da sequência de Gregory-Leibniz: "))

count = 1
res = 0

for i in range(1, n + 1):
  if (i %  2 != 0):
    res += 4 / count
  else: 
    res -= 4 / count
    
  count += 2
  
print(f'O resultado é: {res}')