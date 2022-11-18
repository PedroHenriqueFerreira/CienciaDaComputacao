from components import db

from interface.styles import *


def createBusPopup(popupData):
    ''' Cria um popup para cadastrar um ônibus '''

    return Popup([
        [Title('CADASTRAR ÔNIBUS')],
        [Text('Origem:'), Push(), Input('-ORIGIN-')],
        [Text('Destino:'), Push(), Input('-DESTINY-')],
        [Text('Horário:'), Push(), Input('-START-')],
        [Text('Duração:'), Push(), Input('-DURATION-')],
        [Text('Preço:'), Push(), Input('-PRICE-', '', 'R$ ')],
        [Text('Dia:'), Push(), Input('-DAY-')],
        [
            Button('Voltar', '-CLOSE-', 1),
            Push(),
            Button('Cadastrar ônibus', '-CREATE_BUS-')
        ],
    ])


def updateBusPopup(popupData):
    ''' Cria um popup para atualizar um ônibus '''

    data = db.findById('buses', popupData['selected'])
    
    return Popup([
        [Title('ATUALIZAR ÔNIBUS')],
        [Text('Origem:'), Push(), Input('-ORIGIN-', '', data['origin'])],
        [Text('Destino:'), Push(), Input('-DESTINY-', '', data['destiny'])],
        [Text('Horário:'), Push(), Input('-START-', '', data['start'])],
        [Text('Duração:'), Push(), Input('-DURATION-', '', data['duration'])],
        [Text('Preço:'), Push(), Input('-PRICE-', '', data['price'])],
        [Text('Dia:'), Push(), Input('-DAY-', '', data['day'])],
        [
            Button('Voltar', '-CLOSE-', 1),
            Push(),
            Button('Atualizar ônibus', '-UPDATE_BUS-')
        ],
        [Storage('-SELECTED-', popupData['selected'])],
    ])


def createTicketPopup(popupData):
    ''' Cria um popup para cadastrar um ticket '''

    return Popup([
        [Title('CONFIRMAR COMPRA')],
        [Text('Nome:'), Push(), Input('-NAME-')],
        [Text('Número do cartão:'), Push(), Input('-CARD_NUMBER-')],
        [Text('Vencimento:'), Push(), Input('-EXPIRATION-')],
        [Text('Código de segurança:'), Push(), Input('-CVC-')],
        [
            Button('Voltar', '-CLOSE-', 1),
            Push(),
            Button('Cartão de crédito', '-CREATE_TICKET_CREDIT-', 1),
            Button('Cartão de débito', '-CREATE_TICKET_DEBT-')
        ],
        [Storage('-SELECTED-', popupData['selected'])],
    ])

def errorPopup(popupData):
    ''' Cria um popup de erro '''

    return Popup([
        [Text(popupData['errors'])],
        [
            Push(),
            Button('Certo', '-CLOSE-')
        ]
    ])

def confirmPopup(popupData):
    ''' Cria um popup de confirmação '''

    return Popup([
        [Text(popupData['message'])],
        [
            Push(),
            Button('Cancelar', '-CLOSE-', 2),
            Button(popupData['button'], popupData['key'])
        ],
        [Storage('-SELECTED-', popupData['selected'])],
    ])


def deleteBusConfirm(popupData):
    ''' Cria um popup de confirmação para deletar um ônibus '''

    popupData['message'] = 'Tem certeza que deseja apagar este ônibus?'
    popupData['button'] = 'Apagar ônibus'
    popupData['key'] = '-DELETE_BUS-'

    return confirmPopup(popupData)


def deleteTicketUserConfirm(popupData):
    ''' Cria um popup de confirmação para o usuário deletar um ticket '''

    popupData['message'] = 'Tem certeza que deseja estornar este ticket?'
    popupData['button'] = 'Estornar ticket'
    popupData['key'] = '-DELETE_TICKET-'

    return confirmPopup(popupData)


def deleteTicketCompanyConfirm(popupData):
    ''' Cria um popup de confirmação para a empresa deletar um ticket '''

    popupData['message'] = 'Confirmar o recebimento deste ticket?'
    popupData['button'] = 'Confirmar recebimento'
    popupData['key'] = '-DELETE_TICKET-'

    return confirmPopup(popupData)

# Todos os popups
popups = {
    '-CREATE_BUS_POPUP-': createBusPopup,
    '-UPDATE_BUS_POPUP-': updateBusPopup,
    '-CREATE_TICKET_POPUP-': createTicketPopup,
    '-ERROR_POPUP-': errorPopup,
    
    '-DELETE_BUS_CONFIRM-': deleteBusConfirm,
    '-DELETE_TICKET_USER_CONFIRM-': deleteTicketUserConfirm,
    '-DELETE_TICKET_COMPANY_CONFIRM-': deleteTicketCompanyConfirm,
}
