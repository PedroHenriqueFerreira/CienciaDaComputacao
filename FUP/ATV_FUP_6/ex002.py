compromissos = [
    { 
        'data': { 'dia': 12, 'mes': 'Julho', 'ano': 2022 }, 
        'horario': { 'hora': 9, 'minutos': 30, 'segundos': 0 }, 
        'texto': 'Ir ao médico'
    }
]

def cadastrarCompromissos():
    print('--- Cadastrar Compromisso ---')
    
    horario = { 
        'hora': int(input('Hora: ')), 
        'minutos': int(input('Minutos: ')), 
        'segundos': int(input('Segundos: ')) 
    }
    
    data = { 
        'dia': int(input('Dia: ')), 
        'mes': input('Mês: '), 
        'ano': int(input('Ano: '))
    }
    
    compromisso = { 'data': data, 'horario': horario, 'texto': input('Compromisso: ') }

    compromissos.append(compromisso)

def listarCompromissos():
    print('--- Lista de compromissos ---')
    for compromisso in compromissos:
        data = compromisso['data']
        dataFormatada = f'{data["dia"]} de {data["mes"]} de {data["ano"]}'
        
        horario = compromisso['horario']
        horarioFormatado = f'{horario["hora"]}:{horario["minutos"]}:{horario["segundos"]}'
        
        print(f'{dataFormatada} - {horarioFormatado} - {compromisso["texto"]}')
    
listarCompromissos()