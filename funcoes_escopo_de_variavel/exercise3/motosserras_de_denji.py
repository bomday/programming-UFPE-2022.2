cont = 0
vitoria = 0
derrota = 0
empate= 0 
vilao = ['Makima', 'Reze', 'Santa Claus']
resultado_lista = []
  
def classificacao(e, c, p):
  if e >= 750 and c >= 7 and p >= 8:
    motosserra = 'Motosserra Suprema'
  elif e >= 500 and c >= 6 and p >= 6:
    motosserra = 'Motosserra Avançada'
  else:
    motosserra = 'Motosserra Normal'
  
  return(motosserra)
  
def forca_vencedora(e, c, p, forca_inimigo, inimigo):
  forca_denji = e + (c * p)
  
  if forca_denji > forca_inimigo:
    print(f'Denji saiu vitorioso nessa batalha contra o {inimigo}')
    resultado = 'Vitoria'
  elif forca_denji < forca_inimigo:
    print(f'Denji não conseguiu força o suficiente para derrotar o {inimigo}')
    resultado = 'Derrota'
  else:
    print(f'Como pode ser possível?? Denji possui a mesma força que o {inimigo}')
    resultado = 'Empate'
  
  return(resultado)
  
def mensagem_final(v, d, e):
  if v == 3:
    print('Nenhum dos 3 inimigos foram capazes de derrotar o Denji!')
  elif d == 3:
    print('Hoje não foi um dia bom para o Denji, perdeu todas as batalhas')
  elif v == d == e:
    print('Hoje foi um dia equilibrado para o Denji, conseguiu ganhar, perder e empatar')
  elif v > d and v > e:
    print('Denji conseguiu derrotar a maioria de seus inimigos')
  elif d > v and d > e:
    print('Dia péssimo para o Denji, perdeu a maioria de suas batalhas')
  elif e > v and e > d:
    print('Dia duro para o Denji, empatou de mais')

while cont < 3:
  energia = int(input())
  controle = int(input())
  precisao = int(input())
  inimigo = int(input())
  
  cont = cont + 1
  vilao_atual = vilao[cont-1]
  print(f'### Rodada {cont} - {vilao_atual} ###')
  motosserra = classificacao(energia, controle, precisao)
  print(f'O Denji ira se transformar na {motosserra} para enfrentar o {vilao_atual}')
  resultado = forca_vencedora(energia, controle, precisao, inimigo, vilao_atual)
  resultado_lista.append(f'Rodada {cont}: {motosserra} - {resultado}')
  
  if resultado == 'Vitoria':
    vitoria += 1
  elif resultado == 'Derrota':
    derrota += 1
  elif resultado == 'Empate':
    empate += 1
  
print('### Resultado Final ###')

for elemento in resultado_lista:
  print(elemento)
  
mensagem_final(vitoria, derrota, empate)