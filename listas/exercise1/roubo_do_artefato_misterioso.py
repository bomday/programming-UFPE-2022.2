lista_suspeitos = []
acao = input()

while (acao != 'ja temos nossa lista de suspeitos'):
  if acao == 'novo suspeito - altissima periculosidade':
    suspeito = input()
    lista_suspeitos.insert(0, suspeito)
   
  elif acao == 'novo suspeito - pouco perigoso':
    suspeito = input()
    lista_suspeitos.append(suspeito)
    
  elif acao == 'livre de suspeita, pode remover':
    suspeito = input()
    lista_suspeitos.remove(suspeito)
   
  elif acao == 'sujeito mais perigoso do que pensavamos':
    index_antigo = int(input())
    index_novo = int(input())
    lista_suspeitos[index_antigo], lista_suspeitos[index_novo] = lista_suspeitos[index_novo], lista_suspeitos[index_antigo]
    
  elif acao == 'que estranho, esses dois meliantes… troque-os de lugar':
    #problema em troca de lugares
    suspeito1 = input()
    suspeito2 = input()
    index_suspeito1 = lista_suspeitos.index(suspeito1) 
    index_suspeito2 = lista_suspeitos.index(suspeito2) 
    lista_suspeitos[index_suspeito1], lista_suspeitos[index_suspeito2] = lista_suspeitos[index_suspeito2], lista_suspeitos[index_suspeito1]
    
  elif acao == 'essa posicao nao esta de acordo, ele nao e tao perigoso assim':
    suspeito = input()
    lista_suspeitos.remove(suspeito)
    lista_suspeitos.append(suspeito)
   
  elif acao == 'como a lista esta ficando?':
    
    lista_atual = ''
    suspeito_inicial = True
    for suspeitos in lista_suspeitos:
      if suspeito_inicial == True:
        lista_atual = suspeitos
        suspeito_inicial = False
      else:
        lista_atual = lista_atual + ' ' + suspeitos
    else:
      print(lista_atual)

  acao = input()
else:

  lista_final = ''
  suspeito_inicial = True
  for suspeitos in lista_suspeitos:
    if suspeito_inicial == True:
      lista_final = suspeitos
      suspeito_inicial = False
    else:
      lista_final = lista_final + ' ' + suspeitos  
  else:
    print(f'O resultado final ficou assim:\n{lista_final}')