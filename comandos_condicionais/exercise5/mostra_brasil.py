favoritismoBr = int(input())

oponente1 = input()
favoritismoOponente1 = int(input())
golsBR1 = int(input())
golsOPO1 = int(input())

if golsBR1 < golsOPO1:
  
  print(f'Infelizmente essa seleção dx {oponente1} era muito forte para o Brasil.')

elif golsBR1 > golsOPO1:
  
  if (golsBR1 - golsOPO1) == 1:
    
    favoritismoBr = favoritismoBr + 10
    
  elif (golsBR1 - golsOPO1) == 2:
    
    favoritismoBr = favoritismoBr + 20
    
  else:
    
    favoritismoBr = favoritismoBr + 30
  
  print('Quem é que segura o Brasil???')
  
  oponente2 = input()
  favoritismoOponente2 = int(input())
  golsBR2 = int(input())
  golsOPO2 = int(input())
  
  if golsBR2 < golsOPO2:
    
    print(f'Infelizmente essa seleção dx {oponente2} era muito forte para o Brasil.')
    
  elif golsBR2 > golsOPO2:
    
    if (golsBR2 - golsOPO2) == 1:
      
      favoritismoBr = favoritismoBr + 10
      
    elif (golsBR2 - golsOPO2) == 2:
      
      favoritismoBr = favoritismoBr + 20
      
    else:
      
      favoritismoBr = favoritismoBr + 30
      
    print('Quem é que segura o Brasil???')
    
    oponente3 = input()
    favoritismoOponente3 = int(input())
    golsBR3 = int(input())
    golsOPO3 = int(input())
    
    if golsBR3 < golsOPO3:
      
      print(f'Infelizmente essa seleção dx {oponente3} era muito forte para o Brasil.')
      
    elif golsBR3 > golsOPO3:
      
      if (golsBR3 - golsOPO3) == 1:
        
        favoritismoBr = favoritismoBr + 10
        
      elif (golsBR3 - golsOPO3) == 2:
        
        favoritismoBr = favoritismoBr + 20
        
      else:
        
        favoritismoBr = favoritismoBr + 30
      
      print('Quem é que segura o Brasil???')
      
      oponente4 = input()
      favoritismoOponente4 = int(input())
      
      if favoritismoBr < favoritismoOponente4:
        
        print(f'O nosso Brasil foi vice, não conseguindo bater a seleção dx {oponente4} na simulação')
        
      else: 
        
        print('O BRASIL VAI SER HEXAAAAAAAA')
      
    else:
      
      if favoritismoBr < favoritismoOponente3:
        
        print('Foi no detalhe! Mas infelizmente o Brasil esta eliminado da copa...')
        
      else:
        
        print('No sufoco, o Brasil conseguiu ganhar!!!')
        
        oponente4 = input()
        favoritismoOponente4 = int(input())
        
        if favoritismoBr < favoritismoOponente4:
         
          print(f'O nosso Brasil foi vice, não conseguindo bater a seleção dx {oponente4} na simulação')
          
        else: 
         
          print('O BRASIL VAI SER HEXAAAAAAAA')
    
  else:
    
    if favoritismoBr < favoritismoOponente2:
      
      print('Foi no detalhe! Mas infelizmente o Brasil esta eliminado da copa...')
      
    else:
      
      print('No sufoco, o Brasil conseguiu ganhar!!!')
      
      oponente3 = input()
      favoritismoOponente3 = int(input())
      golsBR3 = int(input())
      golsOPO3 = int(input())
      
      if golsBR3 < golsOPO3:
       
        print(f'Infelizmente essa seleção dx {oponente3} era muito forte para o Brasil.')
       
      elif golsBR3 > golsOPO3:
       
        if (golsBR3 - golsOPO3) == 1:
          
          favoritismoBr = favoritismoBr + 10
         
        elif (golsBR3 - golsOPO3) == 2:
         
          favoritismoBr = favoritismoBr + 20
         
        else:
         
          favoritismoBr = favoritismoBr + 30
       
        print('Quem é que segura o Brasil???')
       
        oponente4 = input()
        favoritismoOponente4 = int(input())
        
        if favoritismoBr < favoritismoOponente4:
          
          print(f'O nosso Brasil foi vice, não conseguindo bater a seleção dx {oponente4} na simulação')
         
        else: 
          
          print('O BRASIL VAI SER HEXAAAAAAAA')
        
      else:
       
        if favoritismoBr < favoritismoOponente3:
         
          print('Foi no detalhe! Mas infelizmente o Brasil esta eliminado da copa...')
         
        else:
         
          print('No sufoco, o Brasil conseguiu ganhar!!!')
         
          oponente4 = input()
          favoritismoOponente4 = int(input())
          
          if favoritismoBr < favoritismoOponente4:
            
            print(f'O nosso Brasil foi vice, não conseguindo bater a seleção dx {oponente4} na simulação')
           
          else: 
            
            print('O BRASIL VAI SER HEXAAAAAAAA')

else:
  
  if favoritismoBr < favoritismoOponente1:
    
    print('Foi no detalhe! Mas infelizmente o Brasil esta eliminado da copa...')
    
  else:
    
    print('No sufoco, o Brasil conseguiu ganhar!!!')
    
    oponente2 = input()
    favoritismoOponente2 = int(input())
    golsBR2 = int(input())
    golsOPO2 = int(input())
    
    if golsBR2 < golsOPO2:
      
      print(f'Infelizmente essa seleção dx {oponente2} era muito forte para o Brasil.')
     
    elif golsBR2 > golsOPO2:
     
      if (golsBR2 - golsOPO2) == 1:
        
        favoritismoBr = favoritismoBr + 10
       
      elif (golsBR2 - golsOPO2) == 2:
       
        favoritismoBr = favoritismoBr + 20
       
      else:
       
        favoritismoBr = favoritismoBr + 30
      
      print('Quem é que segura o Brasil???')
      
      oponente3 = input()
      favoritismoOponente3 = int(input())
      golsBR3 = int(input())
      golsOPO3 = int(input())
     
      if golsBR3 < golsOPO3:
       
        print(f'Infelizmente essa seleção dx {oponente3} era muito forte para o Brasil.')
       
      elif golsBR3 > golsOPO3:
       
        if (golsBR3 - golsOPO3) == 1:
         
          favoritismoBr = favoritismoBr + 10
         
        elif (golsBR3 - golsOPO3) == 2:
         
          favoritismoBr = favoritismoBr + 20
         
        else:
         
          favoritismoBr = favoritismoBr + 30
        
        print('Quem é que segura o Brasil???')
       
        oponente4 = input()
        favoritismoOponente4 = int(input())
        
        if favoritismoBr < favoritismoOponente4:
          
          print(f'O nosso Brasil foi vice, não conseguindo bater a seleção dx {oponente4} na simulação')
          
        else: 
         
          print('O BRASIL VAI SER HEXAAAAAAAA')
       
      else:
       
        if favoritismoBr < favoritismoOponente3:
         
          print('Foi no detalhe! Mas infelizmente o Brasil esta eliminado da copa...')
         
        else:
         
          print('No sufoco, o Brasil conseguiu ganhar!!!')
         
          oponente4 = input()
          favoritismoOponente4 = int(input())
          
          if favoritismoBr < favoritismoOponente4:
            
            print(f'O nosso Brasil foi vice, não conseguindo bater a seleção dx {oponente4} na simulação')
           
          else: 
            
            print('O BRASIL VAI SER HEXAAAAAAAA')
     
    else:
    
      if favoritismoBr < favoritismoOponente2:
       
        print('Foi no detalhe! Mas infelizmente o Brasil esta eliminado da copa...')
       
      else:
       
        print('No sufoco, o Brasil conseguiu ganhar!!!')
       
        oponente3 = input()
        favoritismoOponente3 = int(input())
        golsBR3 = int(input())
        golsOPO3 = int(input())
       
        if golsBR3 < golsOPO3:
         
          print(f'Infelizmente essa seleção dx {oponente3} era muito forte para o Brasil.')
         
        elif golsBR3 > golsOPO3:
         
          if (golsBR3 - golsOPO3) == 1:
           
            favoritismoBr = favoritismoBr + 10
           
          elif (golsBR3 - golsOPO3) == 2:
           
            favoritismoBr = favoritismoBr + 20
            
          else:
            
            favoritismoBr = favoritismoBr + 30
         
          print('Quem é que segura o Brasil???')
         
          oponente4 = input()
          favoritismoOponente4 = int(input())
         
          if favoritismoBr < favoritismoOponente4:
           
            print(f'O nosso Brasil foi vice, não conseguindo bater a seleção dx {oponente4} na simulação')
           
          else: 
            
            print('O BRASIL VAI SER HEXAAAAAAAA')
           
        else:
       
          if favoritismoBr < favoritismoOponente3:
           
            print('Foi no detalhe! Mas infelizmente o Brasil esta eliminado da copa...')
           
          else:
           
            print('No sufoco, o Brasil conseguiu ganhar!!!')
           
            oponente4 = input()
            favoritismoOponente4 = int(input())
           
            if favoritismoBr < favoritismoOponente4:
             
              print(f'O nosso Brasil foi vice, não conseguindo bater a seleção dx {oponente4} na simulação')
             
            else: 
              
              print('O BRASIL VAI SER HEXAAAAAAAA')