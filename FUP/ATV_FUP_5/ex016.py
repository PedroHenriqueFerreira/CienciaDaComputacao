def ordenacaoSelecao(l):
    lista = []
    
    while len(l) > 0:
        min = l[0]
        for i in l:
            if i < min: min = i
        
        lista.append(min)
        l.remove(min)
    
    return lista
