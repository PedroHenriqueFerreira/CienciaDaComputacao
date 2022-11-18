def contaVogais(s):
    count = 0
    
    for i in s:
        if i in 'AEIOUaeiou':
            count += 1
            
    return count