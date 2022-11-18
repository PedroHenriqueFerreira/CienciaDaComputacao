from turtle import Turtle, Screen

def quadrado(c, l):
    c.down()
    
    for _ in range(4):
        c.forward(l)
        c.left(90)
        
    c.up()
    
def quadradoLinha(c, l, n):
    for _ in range(n):
        quadrado(c, l)
        
        c.forward(l * 2)
        
    c.backward(l * n * 2)

def quadradoGrade(c, l, n):
    for i in range(n):
        quadradoLinha(c, l, n)
        
        if (n - 1 != i):
            c.right(90)
            c.forward(l * 2)
            c.left(90)

def quadradoEspiral(c, l, n):
    for _ in range(n):
        for _ in range(4):
            c.forward(l)
            c.left(90)
            
        c.right(360 / n)
        

sc = Screen()

c = Turtle()

# quadrado(c,100)
# quadradoLinha(c, 20, 5)
# quadradoGrade(c,20,5)
quadradoEspiral(c,50,16)

sc.mainloop()