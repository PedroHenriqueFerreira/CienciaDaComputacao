def intersecao(c1,c2):
    lista = []
    for i in c1:
        if i in c2:
            lista.append(i)
            
    return lista

def uniao(c1,c2):
    lista = c2[:]
    
    for i in c1:
        if i not in c2:
            lista.append(i)
            
    return lista

def diferenca(c1,c2):
    lista = []
    for i in c1:
        if i not in c2:
            lista.append(i)
            
    return lista