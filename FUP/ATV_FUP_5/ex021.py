def citacao(nome):
    partes = nome.split(' ');
    newPartes = []
    for i in partes[0: -1]:
        newPartes.append(i[0] + '.')
    
    return partes[-1] + ', ' + ' '.join(newPartes)
