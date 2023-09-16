num_locais = int(input())
melhor_nota = 0
cont = 0
empate = False
melhor_lugar = ''

#computação de pontos para cada lugar
for num_locais in range(0, num_locais): 
  cont = cont + 1
  nome_lugar = input()
  nota = int(input())
  soma_nota = nota
  
  while (nota >= 0):
    nota = int(input())
    if nota >= 0:
      soma_nota = soma_nota + nota
  else: 
    if soma_nota > melhor_nota:
      for cont in range(0):
        pior_nota = melhor_nota
        pior_lugar = melhor_lugar
      
      melhor_nota = soma_nota
      melhor_lugar = nome_lugar
      empate = False
    elif soma_nota < melhor_nota:
      pior_nota = soma_nota
      pior_lugar = nome_lugar
    elif soma_nota == melhor_nota:
      melhor_lugar = melhor_lugar + ", " + nome_lugar
      empate = True

#outputs após todas comparações
else:
  if empate == True:
    print(f'{melhor_lugar}\nTantas opções')
  else:
    print(f'{melhor_lugar} ganhou de lavada de {pior_lugar}, com {melhor_nota} vs {pior_nota}')