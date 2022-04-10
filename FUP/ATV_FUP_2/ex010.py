operation = int(input('1. Soma\n2. Subtração\n3. Multiplicação\n4. Divisão\nSelecionar: '))
num1 = float(input ("1° valor: "))
num2 = float(input ("2° Valor: "))
res = 0

if operation == 1:
    res = num1 + num2
elif operation == 2:
    res = num1 - num2
elif operation == 3:
    res = num1 * num2
else:
    res = num1 / num2

print(f'O resultado é: {res}')