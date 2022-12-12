ini = int(input('Valor inicial: '))
razao = int(input('Razão: '))
qtd = int(input('Quantidade: '))

for i in range(ini, ini + razao * qtd, razao):
  print(i)