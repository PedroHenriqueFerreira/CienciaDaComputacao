product = input('Produto: ')
weight1 = float(input ('Massa da versão 1 (g): '))
price1 = float(input ('Preço da versão 1 (R$): '))
weight2 = float(input ('Massa da versão 2 (g): '))
price2 = float(input ('Preço da versão 2 (R$): '))

if weight1 / price1 > weight2 / price2:
  print(f'{product} de {weight1}g por R${price1:.2f} é mais vantajoso')
else:
  print(f'{product} de {weight2}g por R${price2:.2f} é mais vantajoso')
  