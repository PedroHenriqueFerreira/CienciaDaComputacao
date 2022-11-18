from interface.styles import *
from components.utils import *

from components import db


def welcomePage(pageData):
    ''' Cria uma página de boas vindas '''

    return Page([
        [
            Column([
                [Title('SEJA BEM-VINDO')],
                [Text('Encontre rotas de ônibus com local,\nhorário, compras de ticket e muito mais! \nTudo isso em um só lugar!')],
            ]),
            Column([[
                Image('assets/logo.png')]
            ]),
        ],
        [
            Push(),
            Button('Sou uma empresa', '-SET_COMPANY-', 1),
            Button('Sou um usuário', '-SET_USER-')
        ],
    ])

def loginPage(pageData):
    ''' Cria uma página de login '''
    return Page([
        [Title('ENTRAR'), Push(), Image('assets/logo_small.png')],
        [Text(f'{pageData["ID_TYPE"]}:'), Push(), Input(f'-{pageData["ID_TYPE"]}-')],
        [Text('Senha:'), Push(), Input('-PASSWORD-', '•')],
        [
            Button('Voltar', '-WELCOME_PAGE-', 1),
            Push(),
            Button('Registrar', '-REGISTER_PAGE-', 1),
            Button('Entrar', '-LOGIN-')
        ],
    ])

def registerPage(pageData):
    ''' Cria uma página de registro '''

    return Page([
        [Title('REGISTRAR'), Push(), Image('assets/logo_small.png')],
        [Text('Nome:'), Push(), Input('-NAME-')],
        [Text(f'{pageData["ID_TYPE"]}:'), Push(), Input(f'-{pageData["ID_TYPE"]}-')],
        [Text('Senha:'), Push(), Input('-PASSWORD-', '•')],
        [
            Button('Voltar', '-WELCOME_PAGE-', 1),
            Push(),
            Button('Entrar', '-LOGIN_PAGE-', 1),
            Button('Registrar', '-REGISTER-')
        ],
    ])


def homePage(pageData):
    ''' Cria uma página principal '''

    dbName = 'buses'
    headings = []
    keys = []
    buses = []
    sizes = []
    
    
    if pageData['isCompany']:
        headings = ['#', 'Origem', 'Destino', 'Horário', 'Duração', 'Dia', 'Preço']
        keys = ['id', 'origin', 'destiny', 'start', 'duration', 'day', 'price']
        
        buses = db.find(dbName, {'CNPJ': pageData['CNPJ']}, True)
        sizes = [4, 26, 26, 10, 10, 12, 12]
    else:
        headings = ['#', 'Empresa', 'Origem', 'Destino', 'Horário', 'Duração', 'Dia', 'Preço']
        keys = ['id', 'company', 'origin', 'destiny', 'start', 'duration', 'day', 'price']
        
        buses = db.find(dbName, {'CPF': pageData['CPF']}, True)
        sizes = [4, 14, 19, 19, 10, 10, 12, 12]
    
    data = map(buses, keys)
    allOrigin = [''] + map(buses, 'origin')
    allDestiny = [''] + map(buses, 'destiny')
    
    layout = [
        [
            Image('assets/logo_small.png'),
            Push(),
            Button('Ver tickets', '-TICKETS_PAGE-', 1),
            Button('Sair', '-WELCOME_PAGE-', 2)
        ],
        [
            Title('SEUS DADOS'),
        ],
        [
            Text(f'Nome: {pageData["name"]}'),
            Separator(),
            Text(f'{pageData["ID_TYPE"]}: {pageData[pageData["ID_TYPE"]]}')
        ],
        [Title('LISTA DE ÔNIBUS')],
        [
            Text('Origem: '),
            Select(allOrigin, '-ORIGIN-'),
            Separator(),
            Text('Destino: '),
            Select(allDestiny, '-DESTINY-'),
            Button('Pesquisar', '-SEARCH-')
        ],
        [Table(headings, data, sizes, '-BUSES_TABLE-')],
        [Storage('-KEYS-', str(keys))],
        [Storage('-DB_NAME-', dbName)],
    ]

    if pageData['isCompany']:
        layout.append([
            Push(),
            Button('Apagar ônibus', '-DELETE_BUS_CONFIRM-', 2, True),
            Button('Editar ônibus', '-UPDATE_BUS_POPUP-', 1, True),
            Button('Adicionar ônibus', '-CREATE_BUS_POPUP-')
        ])
    else:
        layout.append([
            Push(),
            Button('Comprar ticket', '-CREATE_TICKET_POPUP-', 0, True)
        ])

    return Page(layout, True)


def ticketsPage(pageData):
    ''' Cria uma página de tickets '''

    tickets = []
    headings = []
    keys = []
    sizes = [4, 8, 19, 19, 19, 10, 10, 11]
    dbName = 'tickets'

    if pageData['isCompany']:
        headings = ['#', 'Código', 'Cliente', 'Origem', 'Destino', 'Horário', 'Dia', 'Preço']
        keys = ['id', 'code', 'user', 'origin', 'destiny', 'start', 'day', 'price']
        tickets = db.find(dbName, {'CNPJ': pageData['CNPJ']}, True)
    else:
        headings = ['#', 'Código', 'Empresa', 'Origem', 'Destino', 'Horário', 'Dia', 'Preço']
        keys = ['id', 'code', 'company', 'origin', 'destiny', 'start', 'day', 'price']        
        tickets = db.find(dbName, {'CPF': pageData['CPF']}, True)
        
    data = map(tickets, keys)
    allOrigin = [''] + map(tickets, 'origin')
    allDestiny = [''] + map(tickets, 'destiny')

    layout = [
        [
            Image('assets/logo_small.png'),
            Push(),
            Button('Ver ônibus', '-HOME_PAGE-', 1),
            Button('Sair', '-WELCOME_PAGE-', 2)
        ],
        [
            Title('SEUS DADOS'),
        ],
        [
            Text(f'Nome: {pageData["name"]}'),
            Separator(),
            Text(f'{pageData["ID_TYPE"]}: {pageData[pageData["ID_TYPE"]]}')
        ],
        [Title('LISTA DE TICKETS')],
        [
            Text('Origem: '),
            Select(allOrigin, '-ORIGIN-'),
            Text('Destino: '),
            Select(allDestiny, '-DESTINY-'),
            Button('Pesquisar', '-SEARCH-')
        ],
        [Table(headings, data, sizes, '-TICKETS_TABLE-')],
        [Storage('-KEYS-', str(keys))],
        [Storage('-DB_NAME-', dbName)],
    ]

    if pageData['isCompany']:
        layout.append([
            Push(),
            Button('Confirmar recebimento',
                   '-DELETE_TICKET_COMPANY_CONFIRM-', 0, True)
        ])
    else:
        layout.append([
            Push(),
            Button('Estornar ticket', '-DELETE_TICKET_USER_CONFIRM-', 0, True)
        ])

    return Page(layout, True)


# Todas as páginas
pages = {
    '-WELCOME_PAGE-': welcomePage,
    '-LOGIN_PAGE-': loginPage,
    '-REGISTER_PAGE-': registerPage,
    '-HOME_PAGE-': homePage,
    '-TICKETS_PAGE-': ticketsPage,
}
