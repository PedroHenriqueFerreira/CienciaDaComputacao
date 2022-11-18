a = int(input("Coeficiente A: "))
b = int(input("Coeficiente B: "))
c = int(input("Coeficiente C: "))

if a == 0:
  print("Não é equação do 2° grau")
else:
  delta = b**2 - 4 * a * c
  x1 = (- b + delta**0.5) / 2 * a
  x2 = (- b - delta**0.5) / 2 * a
  
  if delta < 0:
    print("Não existe raiz real")
  elif delta == 0:
    print(f'Raiz única: {x1}')
  else:
    print(f'Duas raizes: {x1} e {x2}')
    