cod = int(input('Código do produto: '))
qtd = int(input('Quantidade comprada: '))

tot = 0
uni = 0

if 1 <= cod <= 10: 
  uni = 10
  tot = qtd * 10
elif 11 <= cod <= 20:
  uni = 15
  tot = qtd * 15
elif 21 <= cod <= 30:
  uni = 20
  tot = qtd * 20
else:
  uni = 30
  tot = qtd * 30

print(f'Valor unitário: {uni}')
print(f'Valor total da compra: R${tot:.2f}')

if tot <= 250:
  print(f'Desconto: {tot*0.05}')
  tot *= 0.95
elif 250 < tot <= 500:
  print(f'Desconto: {tot*0.1}')
  tot *= 0.9
elif tot > 500:
  print(f'Desconto: {tot*0.15}')
  tot *= 0.85

print(f'Valor final: {tot:.2f}') 
