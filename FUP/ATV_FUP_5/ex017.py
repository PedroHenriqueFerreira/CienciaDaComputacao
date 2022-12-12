def divideNumeros(l,p):
    menores = []
    maiores = []
    
    for i in l:
        if i < p:
            menores.append(i)
        elif i >= p:
            maiores.append(i)
            
    return (menores, maiores)