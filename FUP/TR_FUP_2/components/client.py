from datetime import datetime

from config import storeName, dbPath
from components import db

from components.validate import lenErrors, findErrors, maskErrors
from components.utils import inputData, separator

def register():
    separator('CADASTRAR CLIENTE')
    
    data = inputData({
        'Nome completo': [lenErrors, ('O nome', 3, 50)],
        'Login': [lenErrors, ('O login', 3, 20)],
        'Senha': [lenErrors, ('A senha', 8, 32)],
        'E-mail': [findErrors, ('O e-mail', ['@', '.com'])],
        'Data de nascimento (__/__/____)': [maskErrors, ('A data de nascimento', '##/##/####')],
        'Número do celular (__ _____-____)': [maskErrors, ('O número de celular', '## #####-####')],
        'Endereço para entrega': [lenErrors, ('O endereço', 10, 120)],
    })
    
    if db.find('clients.db', { 'Login': data['Login'] }):
        print('ERRO: Este login já foi criado')
        return
    
    db.create('clients.db', data)
    print('Cliente cadastrado com sucesso')
    
def show():
    separator('MOSTRAR CLIENTE')
    
    data = inputData({ 
        'Login': [lenErrors, ('O login', 3, 20)],
        'Senha': [lenErrors, ('A senha', 8, 32)]
    })
    findData = db.find('clients.db', data)
    
    if not findData:
        print('ERRO: Cliente não encontrado')
        return
    
    for i in findData:
        print(f'{i}: {findData[i]}')
def index():
    separator('MOSTRAR CLIENTES')
    
    findData = db.find('clients.db', {}, True)
    
    for i in findData:
        print(f'Nome completo: {i["Nome completo"]} - Login: {i["Login"]}')
        
def generateReport():
    separator('GERAR RELATÓRIO')
    
    findData = db.find('clients.db', {}, True)
    
    clients = ''

    for i in range(len(findData)):
        clients += f'{i + 1}. {findData[i]["Nome completo"]}\n'
    
    date = datetime.now()
    
    monthString = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro'][date.month - 1]
    
    reportFile = 'clientes.txt'
    
    db.create(reportFile, f'Relatório de clientes\nA loja {storeName} possui {len(findData)} clientes que estão listados abaixo:\n\n{clients}\nRussas, {date.day} de {monthString} de {date.year}')
    
    print(f'Relatório gerado com sucesso em: {dbPath}clientes.txt')