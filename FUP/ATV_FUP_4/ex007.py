from turtle import Turtle, Screen

def espiralQuadrada(c,l,n):
    for i in range(1, n * 2 + 1):
        for _ in range(2):
            c.forward(l * i)
            c.left(90)
            

sc = Screen()

c = Turtle()

espiralQuadrada(c,15,5)

sc.mainloop()