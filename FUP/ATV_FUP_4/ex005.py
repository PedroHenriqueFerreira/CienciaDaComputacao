def trianguloValido(l1, l2, l3):
    if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l2 + l1: 
        return True
    return False

def trianguloTipo(l1, l2, l3):
    if l1 == l2 == l3:
        return 'Equilátero'
    elif l1 != l2 and l2 != l3:
        return 'Escaleno'
    else:
        return 'Isóceles'

l1 = l2 = l3 = 0

while l1 <= 0 or l2 <= 0 or l3 <= 0: 
    l1 = int(input('l1: '))
    l2 = int(input('l2: '))
    l3 = int(input('l3: '))
else:
    if trianguloValido(l1, l2, l3):
        print(trianguloTipo(l1, l2, l3))
    
