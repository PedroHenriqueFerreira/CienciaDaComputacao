import turtle

n = int(input('Quantidade de lados do polígono: '))
l = int(input('Tamanho da linha: '))

sc = turtle.Screen()
turt = turtle.Turtle()

for _ in range(n):
    turt.forward(l)
    turt.right(360/n)
    
sc.mainloop()