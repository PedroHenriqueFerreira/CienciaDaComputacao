import turtle

width = int(input('Tamanho do lado: '))
l = int(input('Quantidade de linhas: '))
col = int(input('Quantidade de colunas: '))

sc = turtle.Screen()
sc.bgcolor('lightgray')
turt = turtle.Turtle()
turt.speed(0)
turt.up()
turt.goto(-sc.window_width()/2, sc.window_height()/2)
turt.down()


for c in range(l):
    for i in range(col):
        if (i % 2 == 0):
            turt.color('black')
        else:
            turt.color('white')
        
        turt.begin_fill()
        for _ in range(4):
            turt.forward(width)
            turt.right(90)
        turt.end_fill()
        turt.forward(width)
    
    if (c % 2 == 0):
        turt.right(90)
        turt.forward(width*2)
        turt.right(90)
    else:
        turt.left(180)

sc.mainloop()