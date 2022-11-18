n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))
n3 = float(input("Nota 3: "))

if not (0 <= n1 <= 10):
    print("A nota 1 é inválida")
elif not (0 <= n2 <= 10):
    print("A nota 2 é inválida")
elif not (0 <= n3 <= 10):
    print("A nota 3 é inválida")
else:
    print("A media das notas é: %.2f"%((n1+n2+n3)/3))
