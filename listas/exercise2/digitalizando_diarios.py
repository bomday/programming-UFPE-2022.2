registros = int(input())
buscador = []

while (registros > 0):
  registros -= 1
  busca = input()
  busca_lista = busca.split(', ')
  buscador.append(busca_lista)

infos = int(input())

while (infos > 0):
  infos -= 1
  conteudo = input()
  
  for assunto in buscador:
    if assunto[0] == conteudo:
      print(f'Informacoes sobre {conteudo} estao no Diario {assunto[1]}')
      break
  else:
    print(f'Nenhum dos diarios possui informacoes sobre {conteudo}')