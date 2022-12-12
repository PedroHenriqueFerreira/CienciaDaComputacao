base = float(input('Salário base: '))
dependentes = float(input('Número de dependentes: '))

tot = base + 120 * dependentes

if 1000 <= tot <= 2500:
    tot *= 0.9
elif tot > 2500:
    tot *= 0.8

if tot <= 1750:
    tot += 500
else:
    tot += 250

print(f'O salário a receber do funcionário é: R${tot:.2f}')