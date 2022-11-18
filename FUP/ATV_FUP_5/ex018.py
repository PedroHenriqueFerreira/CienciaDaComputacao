def combina(l1, l2):
    lista = l1 + l2;
    newLista = []
    count = 0
    
    while len(lista) > 0:
        min = max = lista[0]
        for i in lista:
            if i < min: min = i
            elif i > max: max = i
        
        newLista.insert(count, min)
        
        if min != max:
            newLista.insert(count + 1, max)
            lista.remove(max)
            
        lista.remove(min)
        count += 1 
        
    return newLista

print(combina([1, 3, 5, 6, 8, 14], [2, 3, 5, 22, 54, 55]))