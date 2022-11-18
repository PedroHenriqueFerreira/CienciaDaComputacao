from turtle import Turtle, Screen

def circulo(c, r, cor):
    c.color(cor)
    c.pencolor('black')
    c.right(90)
    c.forward(r)
    c.left(90)
    c.down()
    c.begin_fill()
    c.circle(r)
    c.end_fill()
    c.up()
    c.left(90)
    c.forward(r)
    c.right(90)
            
def aneis(c,r1,r2,n,cor):
    c.color(cor)
    c.pencolor('black')
    c.forward(r2)
    c.left(90)
    
    for _ in range(n):
        c.circle(r2, extent= 360 / n)
        
        c.down()
        c.begin_fill()
        c.circle(r1)
        c.end_fill()
        c.up()
        
    c.left(90)
    c.forward(r2)
    c.left(180)

def alvo(c,r,n,cor1,cor2):
    c.pencolor('black')
    
    for i in range(n, 0, -1):
        
        c.right(90)
        c.forward(r * i)
        c.left(90)
        
        c.color(cor1 if i % 2 == 0 else cor2)
        c.down()
        c.begin_fill()
        c.circle(r * i)
        c.end_fill()
        c.up()
        
        c.left(90)
        c.forward(r * i)
        c.right(90)

sc = Screen()

c = Turtle()
c.up()

# circulo(c,100,"red")
# aneis(c,20,100,32,"red")
alvo(c,10,20,"red","white")

sc.mainloop()