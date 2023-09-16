num_doguinhos = int(input())
doguinhos = {}
aprovado = []
reprovado = []
recu = []

def res_doguinho(atv, obedece, social):
  estrelas = (float(atv) + float(obedece) + float(social))/3
  if estrelas >= 3:
    return 'Aprovado', estrelas
  elif estrelas < 2:
    return 'Reprovado', estrelas
  else:
    return 'Recuperação', estrelas

while num_doguinhos > 0:
  num_doguinhos -= 1
  info_doguinho = input()
  info_doguinho = info_doguinho.split(', ')
  doguinhos[info_doguinho[0]] = [info_doguinho[1], info_doguinho[2], info_doguinho[3], info_doguinho[4]]
  res_dog, estrelas = res_doguinho(doguinhos[info_doguinho[0]][1], doguinhos[info_doguinho[0]][2], doguinhos[info_doguinho[0]][3])

  if res_dog == 'Aprovado':
    aprovado.append([info_doguinho[0], estrelas])
  elif res_dog == 'Reprovado':
    reprovado.append([info_doguinho[0], estrelas])
  elif res_dog == 'Recuperação':
    recu.append([info_doguinho[0], estrelas])

if aprovado != []:
  print('Estao aprovados e de parabens os seguintes coleguinhas:')
  for conteudo in aprovado:
    print(f'{conteudo[0]} - {doguinhos[conteudo[0]][0]} - media: {conteudo[1]:.2f}')

if reprovado != []:
  print('Os colegas a seguir nao se comportaram bem e precisam de ajuda profissional (entrar em contato urgente):')
  for conteudo in reprovado:
    print(f'{conteudo[0]} - {doguinhos[conteudo[0]][0]} - media: {conteudo[1]:.2f}')

if recu != []:
  print('Esses queridos terao uma nova chance e prometem melhorar:')
  for conteudo in recu:
    print(f'{conteudo[0]} - {doguinhos[conteudo[0]][0]} - media: {conteudo[1]:.2f}')