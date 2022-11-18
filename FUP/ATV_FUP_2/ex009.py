a = float(input('Digite um número: '))
b = float(input('Digite um número: '))
c = float(input('Digite um número: '))


if b < a > c:
    if b < c:
        print(f'{b}, {c}, {a}')
    else:
        print(f'{c}, {b}, {a}')
elif a < b > c:
    if a < c:
        print(f'{a}, {c}, {b}')
    else:
        print(f'{c}, {a}, {b}')
else:
    if a < b:
        print(f'{a}, {b}, {c}')
    else:
        print(f'{b}, {a}, {c}')
