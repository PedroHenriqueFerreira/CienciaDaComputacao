from components import db

from components.validators import *

from components.utils import generateCode
    
def login(valores, dadosDaPagina):
    ''' Checa as credenciais do usuário no banco de dados '''
    
    if dadosDaPagina['isCompany']:
        erro = formatErrors([
            checkMaskErrors(valores['-CNPJ-'], 'O CNPJ', '##.###.###/####-##'),
            checkLenErrors(valores['-PASSWORD-'], 'A senha', 8, 32)
        ])

        if erro:
            return { 'errors': erro }

        empresaEncontrada = db.find('companies', {
            'CNPJ': valores['-CNPJ-'], 
            'password': valores['-PASSWORD-']
        })

        if not empresaEncontrada:
            return { 'errors': '• O CNPJ ou a senha estão incorretos' }
        
        return { 'data': empresaEncontrada }
    else:
        erro = formatErrors([
            checkMaskErrors(valores['-CPF-'], 'O CPF', '###.###.###-##'),
            checkLenErrors(valores['-PASSWORD-'], 'A senha', 8, 32)
        ])

        if erro:
            return { 'errors': erro }

        usuarioEncontrado = db.find('users', {
            'CPF': valores['-CPF-'], 
            'password': valores['-PASSWORD-']
        })

        if not usuarioEncontrado:
            return { 'errors': '• O CPF ou a senha estão incorretos' }
        
        return { 'data': usuarioEncontrado }

def register(valores, dadosDaPagina):
    ''' Registra um novo usuário no banco de dados '''
    
    if dadosDaPagina['isCompany']:        
        erro = formatErrors([
            checkLenErrors(valores['-NAME-'], 'O nome', 3, 50),
            checkMaskErrors(valores['-CNPJ-'], 'O CNPJ', '##.###.###/####-##'),
            checkLenErrors(valores['-PASSWORD-'], 'A senha', 8, 32)
        ])

        if erro:
            return { 'errors': erro }

        cpnjEncontrado = db.find('companies', {'CNPJ': valores['-CNPJ-']})
        nomeEncontrado = db.find('companies', { 'name': valores['-NAME-'] })

        if cpnjEncontrado or nomeEncontrado:
            return { 'errors': '• O CNPJ ou o nome já estão em uso' }

        dadosDaEmpresa = {
            'name': valores['-NAME-'], 
            'CNPJ': valores['-CNPJ-'], 
            'password': valores['-PASSWORD-']
        }

        db.create('companies', dadosDaEmpresa)

        return { 'data': dadosDaEmpresa }
    else:
        erro = formatErrors([
            checkLenErrors(valores['-NAME-'], 'O nome', 3, 50),
            checkMaskErrors(valores['-CPF-'], 'O CPF', '###.###.###-##'),
            checkLenErrors(valores['-PASSWORD-'], 'A senha', 8, 32)
        ])

        if erro:
            return { 'errors': erro }

        cpfEncontrado = db.find('users', {'CPF': valores['-CPF-']})
        nomeEncontrado = db.find('users', { 'name': valores['-NAME-'] })

        if cpfEncontrado or nomeEncontrado:
            return { 'errors': '• O CPF ou o nome já estão em uso' }

        dadosDoUsuario = {
            'name': valores['-NAME-'], 
            'CPF': valores['-CPF-'], 
            'password': valores['-PASSWORD-']
        }

        db.create('users', dadosDoUsuario)

        return { 'data': dadosDoUsuario }

def createBus(valores, dadosDaPagina):
    ''' Cria um novo ônibus no banco de dados '''
    
    erro = formatErrors([
        checkLenErrors(valores['-ORIGIN-'], 'A origem', 2, 50),
        checkLenErrors(valores['-DESTINY-'], 'O destino', 2, 50),
        checkMaskErrors(valores['-START-'], 'O horário', '##:##'),
        checkMaskErrors(valores['-DURATION-'], 'A duração', '##:##'),
        checkFindErrors(valores['-PRICE-'], 'O preço', ['R$ ', ',']),
        checkMaskErrors(valores['-DAY-'], 'O dia', '##/##/####')
    ])
    
    if erro:
        return { 'errors': erro }
    
    onibusEncontrado = db.find('buses', { 
        'CNPJ': dadosDaPagina['CNPJ'], 
        'origin': valores['-ORIGIN-'], 
        'destiny': valores['-DESTINY-'], 
        'start': valores['-START-'], 
        'day': valores['-DAY-'] 
    })
    
    if onibusEncontrado:
        return { 'errors': '• Este ônibus já foi adicionado' } 
    
    db.create('buses', { 
        'CNPJ': dadosDaPagina['CNPJ'], 
        'company': dadosDaPagina['name'], 
        'origin': valores['-ORIGIN-'], 
        'destiny': valores['-DESTINY-'], 
        'start': valores['-START-'], 
        'day': valores['-DAY-'], 
        'duration': valores['-DURATION-'], 
        'price': valores['-PRICE-'] 
    })
    
    return {}

def updateBus(valores, dadosDaPagina):
    ''' Atualiza um ônibus no banco de dados '''
    
    erro = formatErrors([
        checkLenErrors(valores['-ORIGIN-'], 'A origem', 2, 50),
        checkLenErrors(valores['-DESTINY-'], 'O destino', 2, 50),
        checkMaskErrors(valores['-START-'], 'O horário', '##:##'),
        checkMaskErrors(valores['-DURATION-'], 'A duração', '##:##'),
        checkFindErrors(valores['-PRICE-'], 'O preço', ['R$ ', ',']),
        checkMaskErrors(valores['-DAY-'], 'O dia', '##/##/####')
    ])
    
    if erro:
        return { 'errors': erro }
    
    db.update('buses', valores['-SELECTED-'], { 
        'CNPJ': dadosDaPagina['CNPJ'],
        'company': dadosDaPagina['name'],
        'origin': valores['-ORIGIN-'], 
        'destiny': valores['-DESTINY-'], 
        'start': valores['-START-'], 
        'day': valores['-DAY-'], 
        'duration': valores['-DURATION-'], 
        'price': valores['-PRICE-'],
    })
    
    return {}

def deleteBus(valores, dadosDaPagina):
    ''' Deleta um ônibus do banco de dados '''
    
    onibusEncontrado = db.findById('buses', valores['-SELECTED-'])
    
    ticketsEncontrados = db.find('tickets', { 
        'CNPJ': onibusEncontrado['CNPJ'], 
        'origin': onibusEncontrado['origin'], 
        'destiny': onibusEncontrado['destiny'], 
        'start': onibusEncontrado['start'], 
        'day': onibusEncontrado['day'] 
    }, True)
    
    for ticketEncontrado in ticketsEncontrados:
        db.delete('tickets', ticketEncontrado['id'])
        
    db.delete('buses', valores['-SELECTED-'])
    
    return {} 

def createTicket(valores, dadosDaPagina):
    ''' Cria um novo ticket no banco de dados '''
    
    erro = formatErrors([
        checkLenErrors(valores['-NAME-'], 'O nome', 3, 50),
        checkMaskErrors(valores['-CARD_NUMBER-'], 'O número do cartão', '#### #### #### ####'),
        checkMaskErrors(valores['-EXPIRATION-'], 'O vencimento', '##/##'),
        checkMaskErrors(valores['-CVC-'], 'O código de segurança', '###'),
    ])
    
    if erro:
        return { 'errors': erro }
    
    onibusEncontrado = db.findById('buses', valores['-SELECTED-'])
    
    db.create('tickets', { 
        'code': generateCode(8), 
        'user': dadosDaPagina['name'], 
        'CPF': dadosDaPagina['CPF'], 
        'CNPJ': onibusEncontrado['CNPJ'],
        'company': onibusEncontrado['company'],
        'origin': onibusEncontrado['origin'],
        'destiny': onibusEncontrado['destiny'],
        'start': onibusEncontrado['start'],
        'duration': onibusEncontrado['duration'],
        'day': onibusEncontrado['day'],
        'price': onibusEncontrado['price'],
    })
    
    return {}

def deleteTicket(valores, dadosDaPagina):
    ''' Deleta um ticket do banco de dados '''
    
    db.delete('tickets', valores['-SELECTED-'])
    
    return {}
    
# Todos os submits
submits = {
    '-LOGIN-': login,
    '-REGISTER-': register,
    '-CREATE_BUS-': createBus,
    '-UPDATE_BUS-': updateBus,
    '-DELETE_BUS-': deleteBus,
    '-CREATE_TICKET_CREDIT-': createTicket,
    '-CREATE_TICKET_DEBT-': createTicket,
    '-DELETE_TICKET-': deleteTicket,
}