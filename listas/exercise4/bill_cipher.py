mensagem = []
alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numeros = list(range(0, 10))
num_palavras = int(input())

for num in range(0, num_palavras):
  enter = input()
  palavra_decodificadora = input()
  enter = input()
  palavra_codificada = input()
  
  if palavra_decodificadora == 'Portal': 
    palavra = ''
    for algoritmo in palavra_codificada:
      for letra in alfabeto:
        if letra == algoritmo:
          if letra == 'z':
            palavra = palavra + alfabeto[0]
          else:
            palavra = palavra + alfabeto[alfabeto.index(algoritmo) + 1]
   
  elif palavra_decodificadora == 'Experimento':
    palavra = 0
    for algoritmo in palavra_codificada:
      for num in numeros:
        if str(num) == algoritmo and num % 2 == 0:
          palavra = palavra + num
    
  elif palavra_decodificadora == 'Realidade':
    palavra = 0
    for algoritmo in palavra_codificada:
      for num in numeros:
        if str(num) == algoritmo and num % 2 == 1:
          palavra = palavra + num
   
  elif palavra_decodificadora == 'Schembulock':
    palavra = 0
    for algoritmo in palavra_codificada:
      for num in numeros:
        if str(num) == algoritmo:
          if palavra == 0:
            palavra = num
          else:
            palavra = palavra * num
  
  if len(str(palavra)) > 0:
    mensagem.append(str(palavra))

mensagem_decodificada = ''
palavra_inicial = True
for palavra in mensagem:
  if palavra_inicial == True:
    mensagem_decodificada = palavra
    palavra_inicial = False
  else:
    mensagem_decodificada = mensagem_decodificada + ' ' + palavra  
else:
  if len(mensagem) == 0:
    print('Esse formato de mensagem nem Bill Cipher entenderia!')
  else:
    print(f'Consegui! A mensagem decodificada de Bill Cipher é: {mensagem_decodificada}')