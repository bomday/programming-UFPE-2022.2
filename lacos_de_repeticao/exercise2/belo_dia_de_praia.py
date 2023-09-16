ato = input()
protetor = False 
dinheiro = 0

while (ato != 'ir para a praia'):
  if ato == 'separar dinheiro':
    dinheiro = float(input()) + dinheiro
  elif ato == 'passar protetor':
    protetor = True
  elif ato == 'choveu':
    clima = 'chuvoso'
  elif ato == 'parou de chover':
    clima = 'ensolarado'
  
  ato = input()
else:
  if clima == 'chuvoso':
    print('Hoje não vai dar pra ir, chuvinha barrou')
  elif clima == 'ensolarado':
    print('Hoje tem sol e mar!')
    
    if protetor == False and dinheiro < 10:
      print('Você não chegou muito bem, chame um médico!')
    elif protetor == False and dinheiro >= 10:
      print('O novo camarão do CIn foi criado')
    elif protetor == True and dinheiro < 10:
      print('Só faltou uma aguinha de coco...')
    elif protetor == True and dinheiro >= 10:
      print('Aí sim! Hoje rendeu!')