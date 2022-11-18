def contaPares(l):
    count = 0
    for i in l:
        if i % 2 == 0: 
            count += 1
    
    return count
