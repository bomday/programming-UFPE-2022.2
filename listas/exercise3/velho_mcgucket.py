mensagem = []
descobrir = int(input())
descobertas = 0

while descobertas < descobrir: #descobrir conteúdo da mensagem a ser decodificada
  descobertas += 1
  
  fibonacci = [0, 1]
  num = 2 
  decodificar = input()
  lista_decodificar = decodificar.split()
  digitos = lista_decodificar[1].split('-')
  
  while num <= int(lista_decodificar[0]): #descobrir número da sequência de fibonacci 
    novo_num = fibonacci[num-1] + fibonacci[num-2]
    fibonacci.append(novo_num)
    num += 1

  num_decodificar = str(fibonacci[-1])
  posicao = 0
  
  for x in num_decodificar: #descobrir número na posição x
    if posicao == int(digitos[0]):
      num_x = x
    
    posicao += 1

  posicao = 0

  for y in num_decodificar: #descobrir número na posição y
    if posicao == int(digitos[1]):
      num_y = y
    
    posicao += 1

  codigo = int(num_x + num_y)
  algoritmo = chr(codigo)
  
  mensagem.append(algoritmo)

else: #formar a mensagem decodificada
  
  mensagem_decodificada = ''
  primeiro_algoritmo = True
  
  for alg in mensagem:
    if primeiro_algoritmo == True:
      mensagem_decodificada = alg
      primeiro_algoritmo = False
    else:
      mensagem_decodificada = mensagem_decodificada + alg  
  else:
    print(mensagem_decodificada)