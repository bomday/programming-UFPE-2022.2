selecao1 = input()
selecao2 = input()
valor_aposta = int(input())
probabilidade = float(input())
resultado = input()

if probabilidade >= 0.5:

  print('Pedro, você está proibido de apostar nos favoritos, só em zebra, lembra?')
  
elif probabilidade < 0.5:
  
  valor_recebido = int(valor_aposta * (1 + (0.5 - probabilidade)**2 * 100))
  
  if 0.4 < probabilidade < 0.5 and 'Ganhou' == resultado:
    
    print(f'Não foi um palpite tão arriscado, todos sabiam que {selecao1} não estava muito atrás de {selecao2}\nParabéns, você apostou R${valor_aposta} e recebeu R${valor_recebido} nessa aposta')
  
  elif 0.3 < probabilidade <= 0.4 and 'Ganhou' == resultado:
    
    print(f'Eu pensava que {selecao2} iria ganhar, mas nunca duvidei que a {selecao1} pudesse ganhar essa partida\nParabéns, você apostou R${valor_aposta} e recebeu R${valor_recebido} nessa aposta')
  
  elif 0.2 < probabilidade <= 0.3 and 'Ganhou' == resultado:
    
    print(f'Uau! que jogo foi esse?? {selecao1} surpreendeu a todos nós…\nParabéns, você apostou R${valor_aposta} e recebeu R${valor_recebido} nessa aposta')
    
  elif 0.1 < probabilidade <= 0.2 and 'Ganhou' == resultado:
    
    print(f'Essa é a copa das zebras?? O impossível aconteceu hoje nessa partida, como que {selecao1} ganhou de {selecao2}, alguém me explica?\nParabéns, você apostou R${valor_aposta} e recebeu R${valor_recebido} nessa aposta')
    
  elif probabilidade <= 0.1 and 'Ganhou' == resultado:
    
    print(f'PEDROOOOO, você tá rico!! ninguém, absolutamente ninguém apostou na {selecao1}, somente você!\nParabéns, você apostou R${valor_aposta} e recebeu R${valor_recebido} nessa aposta')
    
  else: 
    
    print(f'Pedro, infelizmente você está no fundo do poço, se endividou completamente e não temos o que fazer…\nVocê poderia ter ganhado R${valor_recebido}, mas perdeu R${valor_aposta}')