choice = -1

while choice != 5:
  print('''    
---------------------
1. adição
2. subtração
3. multiplicação
4. divisão
5. saída
---------------------
  ''')
  
  choice = int(input('Escolha uma opção: '))
  print()
  
  if choice == 5: break
  
  n1 = int(input('Primeiro valor: '))
  n2 = int(input('Segundo valor: '))
  print()
    
  if choice == 1: print(f'O resultado é {n1 + n2}')
  elif choice == 2: print(f'O resultado é {n1 - n2}')
  elif choice == 3: print(f'O resultado é {n1 * n2}')
  elif choice == 4: print(f'O resultado é {n1 / n2}')
  else: print('Escolha inválida')