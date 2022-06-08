def inverte(s):
    newS = ''
    for i in range(len(s) - 1, -1, -1):
        newS += s[i]
        
    return newS