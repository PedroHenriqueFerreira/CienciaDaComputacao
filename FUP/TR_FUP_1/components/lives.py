from turtle import Turtle
from components import stadium, score
from config import lifeConfig

count = lifeConfig['count']
lives = []

def init():
    ''' Inicia as vidas '''
    
    global lives
    
    lives = []
    
    for i in range(count):
        life = Turtle()
        
        life.speed(0)
        life.up()
        
        life.shape(lifeConfig['shape'])
        life.shapesize(*lifeConfig['size'])
        
        size = life.shapesize()[0] * 20
        
        # Define as posições da arena considerando o tamanho da vida
        stadiumStartX = stadium.startX + size / 2
        stadiumStartY = stadium.startY + size / 2
        
        life.goto(stadiumStartX + i * lifeConfig['padding'] + i * size, stadiumStartY + lifeConfig['marginBottom'])
        
        lives.append(life)
        
def remove():
    ''' Remove uma vida '''
    
    global count
    
    if count > 1:
        count -= 1
        lives[count].hideturtle()
    else:
        count = lifeConfig['count']
        
        for life in lives:
            life.showturtle()
            
        score.setPoints(True)