frase = input()
cont = 1
index = 0
soma_mens = 0
resposta_GPT = ''

def comprimir_mens_user(lista_mens, cont, mens_user):
  quantidade = 1
  if cont >= len(lista_mens):
    if lista_mens[-2] != lista_mens[-1]:
      mens_user = mens_user + str(quantidade) + lista_mens[cont-1]
    
    return mens_user 
  else:
    while cont < len(lista_mens) and lista_mens[cont-1] == lista_mens[cont]:
      cont += 1
      quantidade +=1
    
    mens_user = mens_user + str(quantidade) + lista_mens[cont-1]
    return comprimir_mens_user(lista_mens, cont+1, mens_user)

def soma_mens_gpt(mens, i, soma):
  if i >= len(mens):
    return soma
  else:
    mens_true = False
    if i == 0:
      soma = int(mens[i])
    else:
      for alg in range(0, 10):
        if str(alg) == mens[i]:
          mens_true = True
    
    if i != 0 and mens_true: 
      soma = soma + int(mens[i])
    
    i += 1
    return soma_mens_gpt(mens, i, soma)
  
def descomprimir_mens_GPT(resp_GPT, mens_GPT, i):
  if i>= len(resp_GPT):
    return mens_GPT
  else:
    for cont in range(0, int(resp_GPT[i])):
      mens_GPT = mens_GPT + resp_GPT[i+1]
  
    i += 2
    return descomprimir_mens_GPT(resp_GPT, mens_GPT, i)

while frase != 'Preciso parar de usar o ChatGPT':
  if frase == 'Vou pedir ajuda pro meu amigo ChatGPT':
    mens_descomprimida = input()
    mens_user_final = ''
    mens_descomprimida_GPT = ''
    
    while mens_descomprimida != 'Não tô entendendo nada':
      lista_mens_descomprimida = [alg for alg in mens_descomprimida]
      mens_comprimida_user = comprimir_mens_user(lista_mens_descomprimida, cont, mens_user_final)
      soma_mens_comprimida_gpt = soma_mens_gpt(mens_comprimida_user, index, soma_mens)
      print(f'usuário:{mens_comprimida_user}')
      
      if 0 < soma_mens_comprimida_gpt <= 5:
        resposta_GPT = '1t3a1 1f1a1c3i1n1h1o1 1n3e'
      elif 6 < soma_mens_comprimida_gpt <= 20:
        resposta_GPT = '1c2o2m2p2r3e1 1u3m1 1t2e1c1l1a1d1o1 1n4o1v1o'
      elif 21 < soma_mens_comprimida_gpt <= 30:
        resposta_GPT = '1s6o1 1n1a1 1v1i1d2a1 1m4a1n1s3a'
      elif 31 < soma_mens_comprimida_gpt <= 40:
        resposta_GPT = '1v5a1 1e2s1t4u3d3a3r1 1r1a1p3a3z'
      elif 40 < soma_mens_comprimida_gpt:
        resposta_GPT = '3e1s1t5u1d1a1 1n2a1o1 1p1r3a1 1t2u1 1v4e1r'
      
      print(f'ChatGPT:{resposta_GPT}')
      mens_descomprimida = input()
  elif frase == 'Qual era a tradução?':
    if resposta_GPT == '':
      print('Não tem nada pra traduzir')
    else:
      resposta_descomprimida = descomprimir_mens_GPT(resposta_GPT, mens_descomprimida_GPT, index)
      print(f'Descobri! É: {resposta_descomprimida}, tá de brincadeira né?')

  frase = input() 