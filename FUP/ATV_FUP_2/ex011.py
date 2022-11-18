a = float(input ("A: "))
b = float(input ("B: "))
c = float(input ("C: "))

if (a >= b + c or b >= a + c or c >= b + a):
   print("Os valores nao podem formar um triângulo")
else:
   if (a == b == c):
      print("Equilátero")
   elif (a != b != c):
      print("Escaleno")
   else:
      print("Isóceles")