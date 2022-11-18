from random import randint

def numerosAleatorios(n, min, max):
    lista = []
    
    while len(lista) < n:
        num = randint(min, max - 1)
        if lista.count(num) == 0:
            lista.append(num)
        
    lista.sort()
    
    return lista
