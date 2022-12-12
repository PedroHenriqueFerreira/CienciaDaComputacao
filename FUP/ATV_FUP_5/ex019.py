def removeRepetidas(l: list): 
    lista = l[:]
    for i in range(len(l)):
        if l.index(l[i]) != i:
            lista.remove(l[i])
    
    return lista
