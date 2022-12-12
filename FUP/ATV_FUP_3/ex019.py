n = int(input ("Digite um número: "))

value = 1
prevValue = 0

for i in range(1, n + 1):
  if(i < n):
    print(value, end=', ')
  else:
    print(f'e {value}')
  
  newValue = value
  value = prevValue + value
  prevValue = newValue

print()