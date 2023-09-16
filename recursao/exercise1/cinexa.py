num_pa = input()
lista_num_pa = num_pa.split(' ')
num_pos = int(input())
razao = int(lista_num_pa[1]) - int(lista_num_pa[0])
pos = 1

def descobrir_num(lista, pos_final, pos, r):
  if pos == pos_final:
    num_final = int(lista[0]) + (pos_final - 1) * r
    return num_final
  else:
    num_descoberto = int(lista[0]) + (pos - 1) * r
    pos += 1
    return descobrir_num(lista, pos_final, pos, r)

num_pos_pa = descobrir_num(lista_num_pa, num_pos, pos, razao)
print(f'Na progressão aritmética cujos três primeiros números são {lista_num_pa[0]}, {lista_num_pa[1]} e {lista_num_pa[2]}, o {num_pos}º elemento é {num_pos_pa} e a razão da progressão é {razao}.')