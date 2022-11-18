''' Pedro Henrique Ferreira da Silva | 535770 | CC 2022.1 '''

from turtle import Screen
from components import lives, npc, stadium, character, score, sound
from config import windowConfig, poisonConfig, foodConfig

sound.init(windowConfig['sound'], True, windowConfig['soundDuration'])

window = Screen()

# Retira o delay de atualização da tela
window.tracer(0)

window.title(windowConfig['title'])
window.bgpic(windowConfig["bgPic"])
window.setup(*windowConfig['setup'])

# Importa todas as imagens
for shape in windowConfig['shapes']:
    window.addshape(shape)

# Inicia todos os módulos

stadium.init()
character.init()
lives.init()
score.init()
npc.init(poisonConfig, lives.remove)
npc.init(foodConfig, score.setPoints)

window.listen()

# Mantêm a janela aberta
while True:
    window.update()

''' Créditos: Imagens: https://itch.io | Sons: https://mixkit.co '''
