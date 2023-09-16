meses = [[] for mes in range(0,13)]
num_bichos = int(input())
nome_bicho = {}

while num_bichos > 0:
  num_bichos -=1
  infos = input()
  lista_infos = infos.split(' ')
  lista_data = lista_infos[2].split('/')
  nome_bicho[lista_infos[0]] = lista_infos[1]
  meses[int(lista_data[1])].append(lista_infos[0])
  meses[int(lista_data[1])].sort()

mes_busca = int(input())

if meses[mes_busca] == []:
  print('Sem festa esse mes. :(')
else:
  print('E os donos da festa do mes sao:')
  for bicho in meses[mes_busca]:
    print(f'{bicho} - {nome_bicho[bicho]}')