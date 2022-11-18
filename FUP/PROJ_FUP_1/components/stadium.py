from turtle import Turtle
from config import stadiumConfig

width = stadiumConfig['width']
height = stadiumConfig['height']

startX =  - width / 2 - 2
startY = height / 2 + 2
endX = - startX - 4
endY = - startY + 4

def init():
    ''' Inicia a arena '''
    
    stadium = Turtle()

    stadium.width(stadiumConfig['lineWidth'])
    stadium.speed(0)
    
    stadium.up()
    stadium.goto(startX, startY)
    stadium.down()
    
    for _ in range(2):
        stadium.forward(width)
        stadium.right(90)
        stadium.forward(height)
        stadium.right(90)
    
    stadium.hideturtle()