def ordenacaoSelecao(l):
    lista = []
    count = 0
    
    while len(l) > 0:
        min = max = l[0]
        for i in l:
            if i < min: min = i
            elif i > max: max = i
        
        lista.insert(count, min)
        
        if min != max:
            lista.insert(count + 1, max)
            l.remove(max)
            
        l.remove(min)
        count += 1 
    
    return lista
