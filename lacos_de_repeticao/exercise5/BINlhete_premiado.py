n_binario = int(input())
decimal = 0
cont_binario = 0
chances = 3
acertou = False

while (n_binario != 0):
  resto = n_binario % 10
  decimal = decimal + (resto * (2**cont_binario))
  n_binario = n_binario//10
  cont_binario += 1

while (chances > 0 and acertou == False):
  chances = chances - 1
  palpite = int(input())
  
  if palpite == decimal:
    acertou = True
    print('Parabéns!! Você acertou!')
  elif chances >= 1:
    print(f'Resposta incorreta. Mas não desista! Você ainda tem {chances} chance(s).')
  
else:
  if acertou == False and (decimal == 1 or decimal == 2 or decimal == 3 or decimal == 4 or decimal == 5):
    print('Infelizmente mais uma resposta incorreta.\nAgradecemos sua participação!\nSeu bilhete era premiado. Que pena!')
  elif acertou == False:
    print('Infelizmente mais uma resposta incorreta.\nAgradecemos sua participação!\nPelo menos seu bilhete não era premiado.\nSinta-se à vontade para conhecer nossos pacotes e outras promoções imperdíveis com um de nossos vendedores!')
  else:
    if palpite == 1:
      print('Férias inesquecíveis estão te esperando!\nSeu destino será Porto de Galinhas (BRA).\nPrepare-se para viver dias incríveis desfrutando das riquezas naturais da nossa região!')
    elif palpite == 2:
      print('Férias inesquecíveis estão te esperando!\nSeu destino será Fernando de Noronha (BRA).\nBelíssimas praias estão por vir.\nNão esqueça o protetor solar.')
    elif palpite == 3:  
      print('Férias inesquecíveis estão te esperando!\nSeu destino será Gramado (BRA).\nAproveite passeios e paisagens espetaculares no sul do país!')
    elif palpite == 4:
      print('Férias inesquecíveis estão te esperando!\nSeu destino será Berlim (ALE).\nDesfrute de muita cultura e de experiências incríveis!\nPrepare os casacos de frio!')
    elif palpite == 5:
      print('Férias inesquecíveis estão te esperando!\nSeu destino será Tóquio (JPN).\nViva uma experiência inesquecível explorando um país do outro lado do mundo.\nPrepare-se para muitas horas de voo!')
    else:
      print('Mas, infelizmente, hoje não é o seu dia de sorte.\nApesar de ter dado a resposta correta, seu bilhete não oferece nenhum prêmio.\nSinta-se à vontade para conhecer nossos pacotes e outras promoções imperdíveis com um de nossos vendedores!')