valueMarch = float(input('Valor usado no mês de Março: '))
payMarch = float(input('Valor pago no mês de Março: '))
valueApril = float(input('Valor usado no mês de Abril: '))

restMarch = valueMarch - payMarch
print(f'Fatura do mês de Abril: {valueApril + restMarch + restMarch*0.033}')