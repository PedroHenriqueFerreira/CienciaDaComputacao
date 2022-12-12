from turtle import Turtle, ontimer
from components import stadium, character, sound
from random import randint

def init(npcConfig, onCollision):
    ''' Inicia o NPC '''

    npc = Turtle()
    
    npc.speed(0)
    npc.up()

    speed = npcConfig['speed']

    npc.shapesize(*npcConfig['size'])
    npc.shape(npcConfig['shape'])
    
    sizeWidth = npc.shapesize()[0] * 20
    sizeHeight = npc.shapesize()[1] * 20

    # Define as posições da arena considerando o tamanho do NPC
    stadiumNPCStartX = stadium.startX + sizeWidth / 2 
    stadiumNPCStartY = stadium.startY - sizeHeight / 2
    stadiumNPCEndX = stadium.endX - sizeWidth / 2 
    stadiumNPCEndY = stadium.endY + sizeHeight / 2
    
    def switchRandAngle(currentPlace):
        ''' Escolhe randomicamente um ângulo '''
        
        if currentPlace == 'Right':
            return randint(91, 269)
        elif currentPlace == 'Up':
            return randint(181, 359)
        elif currentPlace == 'Left':
            return [randint(0, 79), randint(271, 359)][randint(0, 1)]
        elif currentPlace == 'Down':
            return randint(1, 179)
    
    def teleport():
        ''' Move o NPC para um lugar randomicamente '''
        
        place = ['Right', 'Up', 'Left', 'Down'][randint(0, 3)]

        if place == 'Right':
            pos = randint(int(stadiumNPCEndY), int(stadiumNPCStartY))
            npc.goto(stadiumNPCEndX, pos)
            npc.setheading(switchRandAngle(place))
        elif place == 'Up':
            pos = randint(int(stadiumNPCStartX), int(stadiumNPCEndX))
            npc.goto(pos, stadiumNPCStartY)
            npc.setheading(switchRandAngle(place))
        elif place == 'Left':
            pos = randint(int(stadiumNPCEndY), int(stadiumNPCStartY))
            npc.goto(stadiumNPCStartX, pos)
            npc.setheading(switchRandAngle(place))
        elif place == 'Down':
            pos = randint(int(stadiumNPCStartX), int(stadiumNPCEndX))
            npc.goto(pos, stadiumNPCEndY)
            npc.setheading(switchRandAngle(place))
    
    def run():
        ''' Faz o NPC avançar sem ultrapassar a arena e sem colidir com o personagem '''
        
        # Define as posições do NPC considerando seu tamanho
        startX = npc.xcor() - sizeWidth / 2
        startY = npc.ycor() + sizeHeight / 2
        endX = npc.xcor() + sizeWidth / 2
        endY = npc.ycor() - sizeHeight / 2
        
        # Colisão com o personagem
        if endX >= character.startX() and startX <= character.endX() and endY <= character.startY() and startY >= character.endY():
            sound.init(npcConfig['sound'])
            teleport()
            onCollision()
        
        # Colisão com a arena
        if startX >= stadium.startX and endX <= stadium.endX and startY <= stadium.startY and endY >= stadium.endY:
            npc.forward(speed)
        else:
            if endX > stadium.endX:
                npc.goto(stadiumNPCEndX, npc.ycor())
                npc.setheading(switchRandAngle('Right'))
            if startY > stadium.startY:
                npc.goto(npc.xcor(), stadiumNPCStartY)
                npc.setheading(switchRandAngle('Up'))
            if startX < stadium.startX:
                npc.goto(stadiumNPCStartX, npc.ycor())
                npc.setheading(switchRandAngle('Left'))
            if endY < stadium.endY:
                npc.goto(npc.xcor(), stadiumNPCEndY)
                npc.setheading(switchRandAngle('Down'))
        
        ontimer(run, 1000 // npcConfig['fps'])

    teleport()
    run()