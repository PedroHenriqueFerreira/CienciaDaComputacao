# Configurações da tela
windowConfig = {
    'setup': (950, 800),
    'shapes': (
        'assets/life.gif', 
        'assets/food.gif',
        'assets/poison.gif',
        *[f'assets/character_right_{i}.gif' for i in range(4)],
        *[f'assets/character_left_{i}.gif' for i in range(4)],
    ),
    'bgPic': 'assets/bg.png',
    'title': 'TRABALHO DE FUP',
    'sound': 'sounds/main.mp3',
    'soundDuration': 97
}

# Configurações da arena
stadiumConfig = {
    'width': 900,
    'height': 600,
    'lineWidth': 4
}

# Configurações do personagem
characterConfig = {
    'size': (2.9285, 4.1),
    'speed': 20,
    'shapes': {
        'right': [f'assets/character_right_{i}.gif' for i in range(4)],
        'left': [f'assets/character_left_{i}.gif' for i in range(4)],
    },
    'sound': 'sounds/teleport.mp3',
}

# Configurações do veneno
poisonConfig = {
    'size': (1.759, 2.15),
    'speed': 8,
    'fps': 50,
    'shape': 'assets/poison.gif',
    'sound': 'sounds/poison.mp3',
}

# Configurações da comida
foodConfig = {
    'size': (1.9545, 2.15),
    'speed': 8,
    'fps': 50,
    'shape': 'assets/food.gif',
    'sound': 'sounds/food.mp3',
}

# Configurações da vida
lifeConfig = {
    'count': 3,
    'marginBottom': 12,
    'padding': 10,
    'size': (1.9445, 1.75),
    'shape': 'assets/life.gif'
}

# Configurações da pontuação
scoreConfig = {
    'marginBottom': 15,
    'font': ('Minecraft', 18, 'normal'),
    'padding': 225,
    'interval': 10,
}