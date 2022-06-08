def repeteVogal(s):
    newS = ''
    
    for i in s:
        if i in 'AEIOUaeiou':
            newS += 2 * i
        else:
            newS += i
            
    return newS