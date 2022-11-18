from os import mkdir, path
from config import dbPath

def find(db, search, all=False):
    ''' Retorna tudo o que tiver no banco db que tenha os parâmetros search '''
    
    if not path.exists(f'{dbPath}{db}'):
        if not path.exists(f'{dbPath}'):
            mkdir(dbPath)
        open(f'{dbPath}{db}', 'a').close()
    
    file = open(f'{dbPath}{db}', 'r')
    
    data = []
    for line in file.readlines():
        line = eval(line)
        
        found = True
        for i in search:
            if search[i] != line[i]:
                found = False
                break
        if found:
            if all:
                data.append(line)
            else:
                return line
    if all:
        return data
    return {}

def create(db, data):
    ''' Cria dados no banco db '''
    
    method = 'a' if '.db' in db else 'w'
    
    file = open(f'{dbPath}{db}', method)
    file.write(f'{data}\n')
    file.close()