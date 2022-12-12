month = int(input('Mês do seu aniversário: '))
day = int(input('Dia do seu aniversário: '))

monthName = ['Mago', 'Arqueiro', 'Suporte', 'Bardo', 'Sniper', 'Gerreiro', 'Fuzileiro', 'MVP', 'Bárbaro', 'NPC', 'PK', 'Noob']

dayName = ['protetor dos novatos', 'domador de dragões', 'lider da guilda', 'especialista de quests', 'que só mata  na faquinha', 'da build errada', 'odiado do server', 'de frag negativo', 'ladrão de kill', 'louco das trocas', 'mendigo de itens', 'que só da rage', 'entendedor de X1', 'que só atrasa a party', 'caçador de bugs', 'expert em headshot', 'fanático das skins', 'perdido no mapa', 'que não acerta nada', 'viciado em mana', 'que carrega o time', 'camper', 'dançarino da safezone', 'anti-hackers', 'que só morre', 'que nunca ajuda o time', 'explorador do mapa', 'que só loga pra conversar', 'que tanka tudo', 'lobo solitário', 'amigo do gm']

print(f'{monthName[month - 1]} {dayName[day - 1]}')