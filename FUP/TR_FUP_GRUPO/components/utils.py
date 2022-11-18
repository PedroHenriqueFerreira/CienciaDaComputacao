from random import randint

def map(valores, chave):
    ''' Mapeia os valores de acordo com a chave passada -> map([{'a':'b'}, {'a': 'c'}], 'a') '''
    
    novosValores = []
    
    for valor in valores:
        if type(chave) == list:
            dados = []
            
            for i in chave:
                dados.append(valor[i])
                
            novosValores.append(dados)    
        else:
            if not valor[chave] in novosValores:
                novosValores.append(valor[chave])
    
    return novosValores

def generateCode(tamanho):
    ''' Gera um código aleatório com o tamanho passado '''
    
    codigo = ''
    caracteres = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    
    for _ in range(tamanho):
        codigo += caracteres[randint(0, len(caracteres) - 1)]    
        
    return codigo

def maskFormat(valor, mascara):
    ''' Transforma o valor no formato da mascara -> maskFormat('12334133333', '###.###.###-##') '''
    
    novoValor = ''
    numeros = '0123456789'
    
    if len(valor) > len(mascara):
        return valor[:len(mascara)]
    
    for i in range(len(valor)):
        if mascara[i] != '#':
            if valor[i] != mascara[i]:
                novoValor += mascara[i]
            if valor[i] in numeros or (valor[i] == mascara[i]):
                novoValor += valor[i]
        elif valor[i] in numeros:
                novoValor += valor[i]
                
    return novoValor