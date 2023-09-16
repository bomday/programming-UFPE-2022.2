selecao1 = input()
selecao2 = input()

gols_selecao1 = 0
gols_selecao2 = 0

if gols_selecao1 < 5:
  entrada1 = input()
  
  if entrada1 == 'Gol': 
    gols_selecao1 += 1

if gols_selecao2 < 5:
  entrada2 = input()
  
  if entrada2 == 'Gol': 
    gols_selecao2 += 1
 
if gols_selecao1 < 5:
  entrada3 = input()
  
  if entrada3 == 'Gol': 
    gols_selecao1 += 1

if gols_selecao2 < 5:
  entrada4 = input()
  
  if entrada4 == 'Gol': 
    gols_selecao2 += 1

if gols_selecao1 < 5:
  entrada5 = input()
  
  if entrada5 == 'Gol': 
    gols_selecao1 += 1

if gols_selecao2 < 5:
  entrada6 = input()
  
  if entrada6 == 'Gol': 
    gols_selecao2 += 1

if gols_selecao1 == 3 and gols_selecao2 == 0:

  vencedor = selecao1
  gols_vencedor = gols_selecao1
  gols_perdedor = gols_selecao2
  
  print(f'{vencedor} vence a disputa de pênaltis por {gols_vencedor} a {gols_perdedor} e avança de fase!')

elif gols_selecao2 == 3 and gols_selecao1 == 0:
  
  vencedor = selecao2
  gols_vencedor = gols_selecao2
  gols_perdedor = gols_selecao1
  
  print(f'{vencedor} vence a disputa de pênaltis por {gols_vencedor} a {gols_perdedor} e avança de fase!')

else: 
  entrada7 = input()

  if entrada7 == 'Gol': 
    gols_selecao1 += 1

  if gols_selecao1 == 3 and gols_selecao2 == 0:
    
    vencedor = selecao1
    gols_vencedor = gols_selecao1
    gols_perdedor = gols_selecao2
    
    print(f'{vencedor} vence a disputa de pênaltis por {gols_vencedor} a {gols_perdedor} e avança de fase!')
    
  elif (gols_selecao2 == 3 and gols_selecao1 == 1) or (gols_selecao2 == 2 and gols_selecao1 == 0):
   
    vencedor = selecao2
    gols_vencedor = gols_selecao2
    gols_perdedor = gols_selecao1
   
    print(f'{vencedor} vence a disputa de pênaltis por {gols_vencedor} a {gols_perdedor} e avança de fase!')
   
  else: 
    entrada8 = input()
    
    if entrada8 == 'Gol':
      gols_selecao2 += 1
   
    if (gols_selecao2 > 3 and gols_selecao1 < 3):
      
      vencedor = selecao2
      gols_vencedor = gols_selecao2
      gols_perdedor = gols_selecao1
      
      print(f'{vencedor} vence a disputa de pênaltis por {gols_vencedor} a {gols_perdedor} e avança de fase!')
     
    elif gols_selecao1 >= 3 and gols_selecao2 <= 1:
      
      vencedor = selecao1
      gols_vencedor = gols_selecao1
      gols_perdedor = gols_selecao2
     
      print(f'{vencedor} vence a disputa de pênaltis por {gols_vencedor} a {gols_perdedor} e avança de fase!')
     
    else:
      entrada9 = input()
     
      if entrada9 == 'Gol': 
        gols_selecao1 += 1
     
      if (gols_selecao1 >= 3 and gols_selecao2 <= 2) or (gols_selecao1 == 5 and gols_selecao2 <= 3):
       
        vencedor = selecao1
        gols_vencedor = gols_selecao1
        gols_perdedor = gols_selecao2
        
        print(f'{vencedor} vence a disputa de pênaltis por {gols_vencedor} a {gols_perdedor} e avança de fase!')
       
      elif (gols_selecao2 >= 3 and gols_selecao1 <= 2) or (gols_selecao2 == 4 and gols_selecao1 <= 3):
       
        vencedor = selecao2
        gols_vencedor = gols_selecao2
        gols_perdedor = gols_selecao1
        
        print(f'{vencedor} vence a disputa de pênaltis por {gols_vencedor} a {gols_perdedor} e avança de fase!')
        
      else:
        entrada10 = input()
        
        if entrada10 == 'Gol': 
          gols_selecao2 += 1
        
        if gols_selecao1 == gols_selecao2:
          
          numero_de_gols = gols_selecao1
          print(f'Ambas as seleções terminaram com {numero_de_gols} gols, mas o desempate vai ficar para outro dia.')
          
        elif gols_selecao1 < gols_selecao2:
         
          vencedor = selecao2
          gols_vencedor = gols_selecao2
          gols_perdedor = gols_selecao1
         
          print(f'{vencedor} vence a disputa de pênaltis por {gols_vencedor} a {gols_perdedor} e avança de fase!')
         
        else:
         
          vencedor = selecao1
          gols_vencedor = gols_selecao1
          gols_perdedor = gols_selecao2
         
          print(f'{vencedor} vence a disputa de pênaltis por {gols_vencedor} a {gols_perdedor} e avança de fase!')