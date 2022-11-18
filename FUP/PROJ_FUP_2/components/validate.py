def lenErrors(value, name, min, max):
    ''' Checa se o tamanho do value está entre min e max '''
    
    if len(value) < min or len(value) > max:
        print(f'ERRO: {name} deve ter entre {min} e {max} caracteres.')
        return False
    return True

def findErrors(value, name, find):
    ''' Checa se o value tem todos os valores de find '''
    
    for i in find:
        if i not in value:
            print(f'ERRO: {name} precisa conter {i}.')
            return False
    return True

def maskErrors(value, name, mask):
    ''' Checa se o value está no formato da mask '''
    
    if len(mask) != len(value):
        print(f'ERRO: {name} é inválid{name[0].lower()}.')
        return False
    
    for i in range(len(mask)):
        if (mask[i] == '#' and value[i] not in '0123456789') or (mask[i] != '#' and value[i] != mask[i]):
            print(f'ERRO: {name} é inválid{name[0].lower()}.')
            return False
        
    return True