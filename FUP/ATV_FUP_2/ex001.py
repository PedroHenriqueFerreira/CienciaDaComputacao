num1 = float(input("Digite um número: "))
num2 = float(input("Digite outro número: "))

if num1 == num2:
  print("Os valores são iguais")
else:
  if num1 > num2:
    print(f"{num1} é maior que {num2}")
  else:
    print(f"{num2} é maior que {num1}")
