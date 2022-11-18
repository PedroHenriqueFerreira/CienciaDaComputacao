from components.utils import *

def formatErrors(erros):
    ''' Formata todos os erros '''

    errosFormatados = []

    for i in range(len(erros)):
        if erros[i] != '':
            errosFormatados.append(f'• {erros[i]}')
    
    if len(errosFormatados) > 0:
        errosFormatados = '\n'.join(errosFormatados)
        return errosFormatados

def checkMaskErrors(valor, campo, mascara):
    ''' Checa se o valor passado está no formato da máscara '''
    
    if len(mascara) != len(valor):
        return f'{campo} deve ter {len(mascara)} caracteres'

    if maskFormat(valor, mascara) != valor:
        return f'{campo} é inválido'
    
    return ''

def checkLenErrors(valor, campo, minimo, maximo):
    ''' Checa se o valor passado está entre o tamanho mínimo e máximo '''
    
    if len(valor) < minimo or len(valor) > maximo:
        return f'{campo} deve ter entre {minimo} e {maximo} caracteres'
    
    return ''
    
def checkFindErrors(valor, campo, itens):
    ''' Checa se o valor passado contém os caracteres da string '''
    
    for item in itens:
        if item not in valor:
            return f'{campo} é inválido'
        
    return ''