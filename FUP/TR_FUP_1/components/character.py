from turtle import Turtle
from components import stadium, sound
from config import characterConfig

sizeWidth = characterConfig['size'][0] * 20
sizeHeight = characterConfig['size'][1] * 20

character = Turtle()

currentFrame = 0
currentStep = 'right'

def init():
    ''' Inicia o personagem '''
    
    character.shapesize(*characterConfig['size'])
    character.shape(characterConfig['shapes'][currentStep][0])
    
    character.speed(0)
    character.up()

    window = character.getscreen()
    
    def run(characterCor, collideCor):
        '''Faz o personagem avançar sem ultrapassar a arena '''
    
        speed = characterConfig['speed']
        
        if characterCor > collideCor:   
            if characterCor - speed > collideCor:
                character.forward(speed)
            else:
                character.forward(characterCor - collideCor) 
        elif characterCor < collideCor: 
            if characterCor + speed < collideCor:
                character.forward(speed)
            else:
                character.forward(collideCor - characterCor)

    def animate():
        global currentFrame
        
        character.shape(characterConfig['shapes'][currentStep][currentFrame])
        
        if currentFrame + 1 < len(characterConfig['shapes'][currentStep]): 
            currentFrame += 1
        else: 
            currentFrame = 0

    def Right():
        ''' Move o personagem para a direita '''
        
        global currentStep
        currentStep = 'right'
        
        animate()
        
        character.setheading(0)
        run(endX(), stadium.endX)

    def Up():
        ''' Move o personagem para cima '''
        
        animate()
        
        character.setheading(90)
        run(startY(), stadium.startY)

    def Left():
        ''' Move o personagem para a esquerda '''
    
        global currentStep
        currentStep = 'left'

        animate()
        
        character.setheading(180)
        run(startX(), stadium.startX)

    def Down():
        ''' Move o personagem para baixo '''
    
        animate()
    
        character.setheading(270)
        run(endY(), stadium.endY)

    window.onkeypress(Right, 'Right')
    window.onkeypress(Up, 'Up')
    window.onkeypress(Left, 'Left')
    window.onkeypress(Down, 'Down')
    
def home():
    ''' Move o personagem para o início '''
    sound.init(characterConfig['sound'])
    
    return character.goto(0, 0)
    
def startX():
    ''' Retorna a posição inicial do X considerando o tamanho do personagem '''
    
    return character.xcor() - sizeWidth / 2

def startY():
    ''' Retorna a posição inicial do Y considerando o tamanho do personagem '''
    
    return character.ycor() + sizeHeight / 2

def endX():
    ''' Retorna a posição final do X considerando o tamanho do personagem '''
    
    return character.xcor() + sizeWidth / 2

def endY():
    ''' Retorna a posição final do Y considerando o tamanho do personagem '''
    
    return character.ycor() - sizeHeight / 2
