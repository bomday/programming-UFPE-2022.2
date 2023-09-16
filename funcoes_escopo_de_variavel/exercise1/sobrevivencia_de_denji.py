lista_primos = []

def primo(n):
  primo = True
  i_primo = True
  
  if n>1:
    for cont in range(2, n):
      if n%cont == 0:
        primo = False
      
      for i in range(2, cont):
        if i == 2:
          i_primo = True
        if cont%i == 0:
          i_primo = False
      
      if i_primo == True:
        lista_primos.append(cont)
  
  def lista_final():
    lista_final = ''
    primo_inicial = True
    for primo in lista_primos:
      if primo_inicial == True:
        lista_final = str(primo)
        primo_inicial = False
      else:
        lista_final = lista_final + ', ' + str(primo)  
    
    return(lista_final)

  if primo == True and n != 1:
    print(f'O número {n} é primo.')
  else:
    print(f'O número {n} não é primo.')
    
    if len(lista_primos) > 0:
      print(f'Entretanto, temos primos no intervalo de 1 à {n}. Estes são:')
      print(lista_final())
      
    else: 
      print(f'Além disso, não temos primos no intervalo de 1 à {n}.')
  
  print('AGORA ESTOU PRONTO PARA MINHA NOVA VIDA!')

n = int(input())

primo(n)