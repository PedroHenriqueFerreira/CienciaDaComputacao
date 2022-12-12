import turtle

a = int(input('Altura de cada camada: '))
b = int(input('Largura da coluna do topo: '))
n = int(input('Quantidade de camadas: '))

sc = turtle.Screen()
turt = turtle.Turtle()

turt.begin_fill()
for i in range(1, n + 1):
  for _ in range(2):
    turt.forward(b*i)
    turt.right(90)
    turt.forward(a)
    turt.right(90)
    
  turt.goto(0, -a*i)
turt.color('green')
turt.end_fill()

sc.mainloop()