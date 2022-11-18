from turtle import Turtle
from components import stadium, character
from config import scoreConfig

matches = Turtle()
record = Turtle()
points = Turtle()

matchesData = recordData = pointsData = 0

def init():   
    ''' Inicia o placar '''

    items = [points, record, matches]

    for i in items:
        i.hideturtle()

        i.speed(0)
        i.up()
        i.goto(stadium.endX - items.index(i) * scoreConfig['padding'], stadium.startY + scoreConfig['marginBottom'])
    
    setPoints(True)


def setPoints(start = False):
    ''' Define o placar '''
    
    global matchesData
    global recordData
    global pointsData
    
    if start: 
        matchesData += 1
        pointsData = 0

        character.home()
        
        matches.clear()
        matches.write(f'Partidas: {matchesData}', font=scoreConfig['font'], align='right')
    else: 
        pointsData += scoreConfig['interval']
    
    if recordData <= pointsData:
        recordData = pointsData
        
        record.clear()
        record.write(f'Recorde: {pointsData}', font=scoreConfig['font'], align='right')
    
    points.clear()
    points.write(f'Pontos: {pointsData}', font=scoreConfig['font'], align='right')
