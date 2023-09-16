jogador1 = input()
bolasGrandeArea1 = int(input())
finalizacoes1 = int(input())
gols1 = int(input())

jogador2 = input()
bolasGrandeArea2 = int(input())
finalizacoes2 = int(input())
gols2 = int(input())

jogador3 = input()
bolasGrandeArea3 = int(input())
finalizacoes3 = int(input())
gols3 = int(input())

if bolasGrandeArea2 < bolasGrandeArea1 and bolasGrandeArea3 < bolasGrandeArea1:
#jogador1 ganha

  if bolasGrandeArea3 < bolasGrandeArea2:
    
    print(f'{jogador1}\n{jogador2}\n{jogador3}')
    
  elif bolasGrandeArea3 > bolasGrandeArea2:
    
    print(f'{jogador1}\n{jogador3}\n{jogador2}')
    
  else:
    
    if ((gols2/finalizacoes2) * 100) > ((gols3/finalizacoes3) * 100):
     
      print(f'{jogador1}\n{jogador2}\n{jogador3}')
     
    else:
      
      print(f'{jogador1}\n{jogador3}\n{jogador2}')

  print('Finalmente o técnico da seleção brasileira liberou a escalação completa do time! O ponta-direita escolhido foi…')
  
  if bolasGrandeArea1 <= 10:
    
    print(f'{jogador1}?! Sei não hein Galvão…')
    
  else:
   
    print(f'{jogador1}! Dessa vez o hexa vem pra casa!!')

elif bolasGrandeArea1 < bolasGrandeArea2 and bolasGrandeArea3 < bolasGrandeArea2:
#jogador2 ganha 

  if bolasGrandeArea1 < bolasGrandeArea3:
    
    print(f'{jogador2}\n{jogador3}\n{jogador1}')
    
  elif bolasGrandeArea1 > bolasGrandeArea3:
    
    print(f'{jogador2}\n{jogador1}\n{jogador3}')
    
  else:
    
    if ((gols3/finalizacoes3) * 100) > ((gols1/finalizacoes1) * 100):
     
      print(f'{jogador2}\n{jogador3}\n{jogador1}')
     
    else:
      
      print(f'{jogador2}\n{jogador1}\n{jogador3}')

  print('Finalmente o técnico da seleção brasileira liberou a escalação completa do time! O ponta-direita escolhido foi…')

  if bolasGrandeArea2 <= 10:
    
    print(f'{jogador2}?! Sei não hein Galvão…')
    
  else:
   
    print(f'{jogador2}! Dessa vez o hexa vem pra casa!!')

elif bolasGrandeArea2 < bolasGrandeArea3 and bolasGrandeArea1 < bolasGrandeArea3:
#jogador3 ganha

  if bolasGrandeArea1 < bolasGrandeArea2:
    
    print(f'{jogador3}\n{jogador2}\n{jogador1}')
    
  elif bolasGrandeArea1 > bolasGrandeArea2:
    
    print(f'{jogador3}\n{jogador1}\n{jogador2}')
    
  else:
    
    if ((gols2/finalizacoes2) * 100) > ((gols1/finalizacoes1) * 100):
     
      print(f'{jogador3}\n{jogador2}\n{jogador1}')
     
    else:
      
      print(f'{jogador3}\n{jogador1}\n{jogador2}')

  print('Finalmente o técnico da seleção brasileira liberou a escalação completa do time! O ponta-direita escolhido foi…')

  if bolasGrandeArea3 <= 10:
    
    print(f'{jogador3}?! Sei não hein Galvão…')
    
  else:
   
    print(f'{jogador3}! Dessa vez o hexa vem pra casa!!')

  
elif bolasGrandeArea3 < bolasGrandeArea2 == bolasGrandeArea1:
#jogador1 e jogador2 empate 

  print('Tite está mais indeciso do que nunca!')
  
  if ((gols1/finalizacoes1) * 100) > ((gols2/finalizacoes2) * 100):
    
    print(f'{jogador1}\n{jogador2}\n{jogador3}')
    print('Finalmente o técnico da seleção brasileira liberou a escalação completa do time! O ponta-direita escolhido foi…')
    
    if bolasGrandeArea1 <= 10:
     
      print(f'{jogador1}?! Sei não hein Galvão…')
     
    else:
     
      print(f'{jogador1}! Dessa vez o hexa vem pra casa!!')
    
  else:
    
    print(f'{jogador2}\n{jogador1}\n{jogador3}')
    print('Finalmente o técnico da seleção brasileira liberou a escalação completa do time! O ponta-direita escolhido foi…')
    
    if bolasGrandeArea2 <= 10:
     
      print(f'{jogador2}?! Sei não hein Galvão…')
     
    else:
     
      print(f'{jogador2}! Dessa vez o hexa vem pra casa!!')

elif bolasGrandeArea2 < bolasGrandeArea3 == bolasGrandeArea1:
#jogador3 e jogador1 empate 

  print(f'Tite está mais indeciso do que nunca!')
  
  if ((gols1/finalizacoes1) * 100) > ((gols3/finalizacoes3) * 100):
    
    print(f'{jogador1}\n{jogador3}\n{jogador2}')
    print('Finalmente o técnico da seleção brasileira liberou a escalação completa do time! O ponta-direita escolhido foi…')
    
    if bolasGrandeArea1 <= 10:
     
      print(f'{jogador1}?! Sei não hein Galvão…')
      
     
    else:
     
      print(f'{jogador1}! Dessa vez o hexa vem pra casa!!')
    
  else:
    
    print(f'{jogador3}\n{jogador1}\n{jogador2}')
    print('Finalmente o técnico da seleção brasileira liberou a escalação completa do time! O ponta-direita escolhido foi…')
    
    if bolasGrandeArea3 <= 10:
     
      print(f'{jogador3}?! Sei não hein Galvão…')
     
    else:
     
      print(f'{jogador3}! Dessa vez o hexa vem pra casa!!')

elif bolasGrandeArea1 < bolasGrandeArea2 == bolasGrandeArea3:
#jogador3 e jogador2 empate 

  print('Tite está mais indeciso do que nunca!')
 
  if ((gols2/finalizacoes2) * 100) > ((gols3/finalizacoes3) * 100):
    
    print(f'{jogador2}\n{jogador3}\n{jogador1}')
    print('Finalmente o técnico da seleção brasileira liberou a escalação completa do time! O ponta-direita escolhido foi…')
    
    if bolasGrandeArea2 <= 10:
     
      print(f'{jogador2}?! Sei não hein Galvão…')
     
    else:
     
      print(f'{jogador2}! Dessa vez o hexa vem pra casa!!')
    
  else:
    
    print(f'{jogador3}\n{jogador2}\n{jogador1}')
    print('Finalmente o técnico da seleção brasileira liberou a escalação completa do time! O ponta-direita escolhido foi…')
    
    if bolasGrandeArea3 <= 10:
     
      print(f'{jogador3}?! Sei não hein Galvão…')
     
    else:
     
      print(f'{jogador3}! Dessa vez o hexa vem pra casa!!')

else: 
#todos empatados

  print('Tite está mais indeciso do que nunca!')
 
  if ((gols1/finalizacoes1) * 100) > ((gols2/finalizacoes2) * 100) and ((gols1/finalizacoes1) * 100) > ((gols3/finalizacoes3) * 100):
    #jogador1 ganha
    
    if ((gols2/finalizacoes2) * 100) > ((gols3/finalizacoes3) * 100):
      
      print(f'{jogador1}\n{jogador2}\n{jogador3}')
      
    else:
      
      print(f'{jogador1}\n{jogador3}\n{jogador2}')
   
    print('Finalmente o técnico da seleção brasileira liberou a escalação completa do time! O ponta-direita escolhido foi…')
    
    if bolasGrandeArea1 <= 10:
     
      print(f'{jogador1}?! Sei não hein Galvão…')
     
    else:
     
      print(f'{jogador1}! Dessa vez o hexa vem pra casa!!')
    
  elif ((gols2/finalizacoes2) * 100) > ((gols1/finalizacoes1) * 100) and ((gols2/finalizacoes2) * 100) > ((gols3/finalizacoes3) * 100):
    #jogador2 ganha
    
    if ((gols1/finalizacoes1) * 100) > ((gols3/finalizacoes3) * 100):
      
      print(f'{jogador2}\n{jogador1}\n{jogador3}')
      
    else:
      
      print(f'{jogador2}\n{jogador3}\n{jogador1}')
   
    print('Finalmente o técnico da seleção brasileira liberou a escalação completa do time! O ponta-direita escolhido foi…')
    
    if bolasGrandeArea2 <= 10:
     
      print(f'{jogador2}?! Sei não hein Galvão…')
     
    else:
     
      print(f'{jogador2}! Dessa vez o hexa vem pra casa!!')
    
  else:
    #jogador3 ganha
    
    if ((gols2/finalizacoes2) * 100) > ((gols1/finalizacoes1) * 100):
      
      print(f'{jogador3}\n{jogador2}\n{jogador1}')
      
    else:
      
      print(f'{jogador3}\n{jogador1}\n{jogador2}')
   
    print('Finalmente o técnico da seleção brasileira liberou a escalação completa do time! O ponta-direita escolhido foi…')
    
    if bolasGrandeArea3 <= 10:
     
      print(f'{jogador3}?! Sei não hein Galvão…')
     
    else:
     
      print(f'{jogador3}! Dessa vez o hexa vem pra casa!!')