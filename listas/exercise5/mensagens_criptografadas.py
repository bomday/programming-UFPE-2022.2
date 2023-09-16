inimigo = input()
aliado = input()
clima = input()
lista_geral = []
mensagem = ''

while mensagem != 'Cansado': #para formar lista geral com lista de números dentro
  mensagem = input()
  lista_mensagem = mensagem.split(' ')
  
  if mensagem != 'Cansado':
    lista_geral.append(lista_mensagem)

if clima == 'Ensolarado' or clima == 'Nublado' or clima == 'ChuvosoNormal' or clima == 'ChuvosoComRaio':
  if clima == 'Ensolarado':
    for organizar in range(0, 10): #loop para ajudar a comparar números e ter certeza de que a lista estará em ordem crescente
      for lista in lista_geral: #organiza as listas dentro da lista geral
        for cont in range(len(lista)):
          if lista[cont] == lista[-1]:
            break 
          elif int(lista[cont]) > int(lista[cont + 1]):
            lista[cont], lista[cont + 1] = lista[cont + 1], lista[cont] 
    
    print(f'Caramba! Finalmente organizamos a mensagem secreta do {inimigo} com esse clima Ensolarado! Vamos nessa {aliado}!')
    
  elif clima == 'Nublado':
    for organizar in range(0, 10): #loop para ajudar a comparar números e ter certeza de que a lista estará em ordem decrescente
      for lista in lista_geral: #organiza as listas dentro da lista geral
        for cont in range(len(lista)):
          if lista[cont] == lista[-1]:
            break 
          elif int(lista[cont]) < int(lista[cont + 1]):
            lista[cont + 1], lista[cont] = lista[cont], lista[cont + 1]
    
    print(f'Ufa! Mesmo com o clima Nublado ainda desvendamos a mensagem do {inimigo}! Vamos nessa {aliado}!')
    
  elif clima == 'ChuvosoNormal':
    for cont in range(len(lista_geral[0])): #repetir em um intervalo do tamanho da lista que é igual em todos os casos
      num_lista = 0
      for comparar in range(len(lista_geral)-1): #repetir comparação por número de listas menos um vezes
        if int(lista_geral[num_lista][cont]) < int(lista_geral[num_lista + 1][cont]):
          lista_geral[num_lista][cont], lista_geral[num_lista + 1][cont] = lista_geral[num_lista + 1][cont], lista_geral[num_lista][cont]
        
        num_lista += 1
    
    print(f'Nem mesmo a chuva vai nos parar de salvar o mundo! Desvendamos a mensagem do {inimigo}! Vamos nessa {aliado}!')
    
  elif clima == 'ChuvosoComRaio':
    for cont in range(len(lista_geral[0])): #repetir em um intervalo do tamanho da lista que é igual em todos os casos
      num_lista = 0
      for comparar in range(len(lista_geral)-1): #repetir comparação por número de listas menos um vezes
        if int(lista_geral[num_lista][cont]) > int(lista_geral[num_lista + 1][cont]):
          lista_geral[num_lista][cont], lista_geral[num_lista + 1][cont] = lista_geral[num_lista + 1][cont], lista_geral[num_lista][cont]
        
        num_lista += 1
    
    print(f'Eitaa! Até mesmo essa chuva com trovoadas não nos parou. Estamos indo até você, {inimigo}! Vamos nessa {aliado}!')

  print(f'Agora decodificamos as {len(lista_geral)} mensagens do {inimigo} e sabemos seus {len(lista_geral)} lugares de ataque.\nOs lugares sao:')

  posicao = 0 

  for mensagem_posicao in range(len(lista_geral)): #definir detalhes de cada mensagem
    posicao = posicao + 1
    print(f'{posicao} lugar:')
    print(f'Coordenadas: {lista_geral[mensagem_posicao][0]}° {lista_geral[mensagem_posicao][1]}\' {lista_geral[mensagem_posicao][2]}\'\'')
    print(f'Horario: {lista_geral[mensagem_posicao][3]}h {lista_geral[mensagem_posicao][4]}m {lista_geral[mensagem_posicao][5]}s')
    print(f'Data: {lista_geral[mensagem_posicao][6]}/{lista_geral[mensagem_posicao][7]}/{lista_geral[mensagem_posicao][8]}')

  print(f'Vamos rapido {aliado}!!')
  
else:
  print(f'Infelizmente esse clima não está bom. Não conseguimos decifrar a mensagem, o que será do mundo agora??\nTenho certeza que conseguiremos na próxima {aliado}')