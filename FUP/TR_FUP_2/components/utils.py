def inputData(data):
    ''' Lê todas as chaves do data enquanto não houver erros '''
    
    for i in data:
        value = input(f'{i}: ')
        item = data[i]

        while not item[0](value, *item[1]):
            value = input(f'{i}: ')

        data[i] = value
        
    return data


def separator(value, char='-'):
    ''' Mostra o value centralizado entre vários char '''
    
    LEN = (50 - len(value) - 2) // 2
    
    print(f'{char * LEN} {value} {char * LEN}')