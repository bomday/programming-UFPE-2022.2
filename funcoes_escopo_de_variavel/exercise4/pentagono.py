celas_ordens = input()
lista_celas_ordens = celas_ordens.split(' ')
lista_prisioneiros = []

def indice_cela(prisioneiro, celas): #retorna índice
  soma = 0
  
  for letra in prisioneiro:
    soma = soma + ord(letra)

  indice = soma % int(celas)
  return(indice)

demonio_cela = 0

def alteracao_adicao(nome, i, celas_total): #faz alteração adicionando prisioneiro
  global demonio_cela
  
  if lista_prisioneiros[i] == '':
    lista_prisioneiros[i] = nome
  else:
    while lista_prisioneiros[i] != '':
      i =  (i + 1) % int(celas_total)
    else: 
      lista_prisioneiros[i] = nome
  
  demonio_cela += 1

def alteracao_remocao(nome, i, celas_total): #faz alteração removendo prisioneiro
  global demonio_cela 
  
  if lista_prisioneiros[i] == nome:
    lista_prisioneiros[i] = ''
    demonio_cela -= 1
  else:
    if nome not in lista_prisioneiros:
      print('NAO EXISTE')
    else:
      indice_nome = lista_prisioneiros.index(nome)
      lista_prisioneiros[indice_nome] = ''
      demonio_cela -= 1

for elemento in range(0, int(lista_celas_ordens[0])): #cria lista de celas
  lista_prisioneiros.append('')

cont = 0

for cont in range(0, int(lista_celas_ordens[1])): #confere ordens
  ordem_nome = input()
  lista_ordem_nome = ordem_nome.split(' ')
  indice_prisao = indice_cela(lista_ordem_nome[1], lista_celas_ordens[0])
  
  if lista_ordem_nome[0] == 'ADICIONAR':
    if demonio_cela == int(lista_celas_ordens[0]):
      print('CHEIO')
    else:
      alteracao_adicao(lista_ordem_nome[1], indice_prisao, lista_celas_ordens[0])
  elif lista_ordem_nome[0] == 'REMOVER':
    alteracao_remocao(lista_ordem_nome[1], indice_prisao, lista_celas_ordens[0])

mensagem_demonios = ''
mensagem = 0
  
for demonio_preso in lista_prisioneiros:
  if demonio_preso != '' and mensagem == 0:
    mensagem_demonios = demonio_preso
    mensagem += 1
  elif demonio_preso != '':
    mensagem_demonios = mensagem_demonios + ' ' + demonio_preso

print(mensagem_demonios)