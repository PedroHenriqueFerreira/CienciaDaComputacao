def limites(l):
    min = max = l[0]
    for i in l:
        if i < min: min = i
        elif i > max: max = i
        
    return (min, max)