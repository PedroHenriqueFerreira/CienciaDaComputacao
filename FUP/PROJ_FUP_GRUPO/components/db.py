from os import mkdir
from os.path import exists

pasta = 'database/'
extensao = '.db'

def create(nomeDoBanco, novosDados):
    ''' Cria no banco de dados um novo registro -> create('usuarios', { 'nome': 'Vitor' }) '''
    arquivo = open(f'{pasta}{nomeDoBanco}{extensao}', 'a')
    arquivo.write(f'{str(novosDados)}\n')
    arquivo.close()

def find(nomeDoBanco, pesquisa, mostrarTodos=False):
    ''' Busca no banco de dados os registros passados -> find('usuarios', { 'nome': 'Joao' }, True) '''
    
    if not exists(f'{pasta}{nomeDoBanco}{extensao}'):
        # Cria a pasta caso não exista
        if not exists(pasta):
            mkdir(pasta)
            
        # Cria o arquivo
        open(f'{pasta}{nomeDoBanco}{extensao}', 'a').close()
    
    arquivo = open(f'{pasta}{nomeDoBanco}{extensao}', 'r')
    
    dados = []
    linhas = arquivo.readlines()
    
    for i in range(len(linhas)):
        linha = eval(linhas[i].strip())
        linha['id'] = i + 1
        
        adicionar = True
        for item in pesquisa:
            if item in linha:
                if pesquisa[item] != '':
                    if pesquisa[item] != linha[item]:
                        adicionar = False
                        break
        
        if adicionar:
            if mostrarTodos:
                dados.append(linha)
            else:
                arquivo.close()
                return linha
    arquivo.close()
    
    if mostrarTodos:
        return dados
    
    return {}

def findById(nomeDoBanco, id):
    ''' Busca no banco de dados o registro com o id passado -> findById('usuarios', 4) '''
    
    dadosDoBanco = find(nomeDoBanco, {}, True)
    
    for i in range(len(dadosDoBanco)):
        if int(id) - 1 == i:
            return dadosDoBanco[i]
    return {}

def update(nomeDoBanco, id, novosDados):
    ''' Atualiza no banco de dados o registro com o id passado -> update('usuarios', 4, { 'nome': 'Carlos' }) '''
    
    dadosDoBanco = find(nomeDoBanco, {}, True)
    arquivo = open(f'{pasta}{nomeDoBanco}{extensao}', 'w')
    
    dadosDoBanco[int(id) - 1] = novosDados
    
    for dadoDoBanco in dadosDoBanco:
        if 'id' in dadoDoBanco:
            del dadoDoBanco['id']
        arquivo.write(f'{str(dadoDoBanco)}\n')

    arquivo.close()

def delete(nomeDoBanco, id):
    ''' Deleta no banco de dados o registro com o id passado -> delete('usuarios', 5) '''
    
    dadosDoBanco = find(nomeDoBanco, {}, True)
    arquivo = open(f'{pasta}{nomeDoBanco}{extensao}', 'w')
    
    dadosDoBanco.pop(int(id) - 1)

    for dadoDoBanco in dadosDoBanco:
        del dadoDoBanco['id']
        
        arquivo.write(f'{str(dadoDoBanco)}\n')
    
    arquivo.close()