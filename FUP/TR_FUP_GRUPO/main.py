''' 
    Pedro Henrique Ferreira da Silva | 535770 | CC 2022.1
    Vitor Freitas de Meneses | 538057 | CC 2022.1
    Filipe Gomes Martins de Souza | 537165 | CC 2022.1
    Éverton da Cunha Sousa | 537858 | CC 2022.1
'''

import PySimpleGUI as sg

from interface.pages import pages
from interface.popups import popups
from components.submits import submits

from components.validators import *
from components.utils import *

from components import db

from config import maskConfig

# Abre a página de boas vindas
openedPage = pages['-WELCOME_PAGE-']({})

openedPopup = None
openedErrorPopup = None

# Dados da página
pageData = {}

# Dados dos popups
popupData = {}

while True:
    window, event, values = sg.read_all_windows()
    
    if event in [sg.WIN_CLOSED, '-CLOSE-']:
        ''' Fecha o programa '''
        
        window.close()
        
        if window != openedPage:
            continue
        break       
     
    if 'SET' in event:
        ''' Define o tipo de usuário '''
        
        pageData['isCompany'] = 'COMPANY' in event        
        ID_TYPES = ['CPF', 'CNPJ']
                
        for i in pageData.copy():
            if i in ID_TYPES:
                del pageData[i]
                    
        pageData['ID_TYPE'] = ID_TYPES[pageData['isCompany']]
        event = '-LOGIN_PAGE-'
    
    if event in maskConfig:
        ''' Aplica a máscara de formatação '''
        
        newValue = maskFormat(values[event], maskConfig[event])
        
        if newValue != values[event]:
            window[event].update(newValue)    
        
    if event in submits:
        ''' Submete um formulário '''
        
        result = submits[event](values, pageData)
        
        if 'errors' in result:
            popupData['errors'] = result['errors']
            event = '-ERROR_POPUP-'
        else:
            if 'data' in result:
                for i in result['data']:
                    pageData[i] = result['data'][i]
                    
            if window == openedPopup:          
                for i in openedPage.AllKeysDict:
                    if 'TABLE' in i:
                        keys = openedPage['-KEYS-'].DefaultText
                        dbName = openedPage['-DB_NAME-'].DefaultText
                        
                        data = db.find(dbName, { 
                            pageData['ID_TYPE']: pageData[pageData['ID_TYPE']] 
                        }, True)
                        
                        openedPage[i].update(map(data, eval(keys)))
                        
                        openedPage['-ORIGIN-'].update(values=[''] + map(data, 'origin'))
                        openedPage['-DESTINY-'].update(values=[''] + map(data, 'destiny'))
                        
                        event = i
                        values[i] = []
                        
                window.close()
            else:
                event = '-HOME_PAGE-'
    
    if 'TABLE' in event:
        ''' Obtém o id do registro selecionado '''
        
        isSelected = len(values[event]) > 0
        
        if isSelected:
            selectedRow = values[event][0]
            popupData['selected'] = openedPage[event].Values[selectedRow][0]
        
        for i in openedPage.AllKeysDict:
            if ('CONFIRM' in i or 'POPUP' in i) and 'CREATE_BUS' not in i:
                openedPage[i].update(disabled=not isSelected)
    
    if event == '-SEARCH-':
        ''' Busca um registro '''
        
        keys = values['-KEYS-']
        dbName = values['-DB_NAME-']
        
        for i in openedPage.AllKeysDict:
            if 'TABLE' in i:
                
                data = db.find(dbName, {
                    'origin': values['-ORIGIN-'],
                    'destiny': values['-DESTINY-'],
                    pageData['ID_TYPE']: pageData[pageData['ID_TYPE']]
                }, True)
                
                openedPage[i].update(map(data, eval(keys)))

    if event in pages:
        ''' Abre uma página '''
        
        openedPage.close()
        openedPage = pages[event](pageData)    

    if event in popups:
        ''' Abre um popup '''
        
        if event == '-ERROR_POPUP-': 
            if openedErrorPopup:
                openedErrorPopup.close()
                
            openedErrorPopup = popups[event](popupData)
        else:
            if openedPopup:
                openedPopup.close()
            
            openedPopup = popups[event](popupData)    

window.close()
