def menorFrente(l):
    min = l[0]
    for i in l:
        if i < min:
            min = i
        
    lista = l[:]
    lista.remove(min)
    lista.insert(0, min)
    
    return lista
    