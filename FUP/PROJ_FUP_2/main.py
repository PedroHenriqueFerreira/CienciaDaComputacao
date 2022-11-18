''' Pedro Henrique Ferreira da Silva | 535770 | CC 2022.1 '''

from config import storeName
from components import client

from components.utils import separator

while True:
    separator(storeName)
    
    res = input('[1] Cadastrar cliente\n[2] Mostrar dados do cliente\n[3] Mostrar clientes cadastrados\n[4] Gerar relatório dos clientes\n[0] Sair\n\nOpção: ')
    
    if res == '1':
        client.register()
    elif res == '2':
        client.show()
    elif res == '3':
        client.index()
    elif res == '4':
        client.generateReport()
    elif res == '0':
        break
    else:
        print('ERRO: Valor inválido')