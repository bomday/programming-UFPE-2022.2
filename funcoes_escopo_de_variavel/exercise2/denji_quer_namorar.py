percentagem_alta  = []
percentagem_baixa  = []
num_baixa = []
nome = ''
  
def resultado(nome): #função para output de acordo com o tamanho do nome
  if nome == "Makima":
    print("Woof Woof")

  if len(nome) > 7:
    menina = [letra for letra in nome]
    print(f"Er {menina[0]}{menina[1]}.. errr... nao consigo lembrar, melhor deixar para la")
  else:
    percentagem = int(input())
    return(percentagem)

def probabilidade(percentagem, nome): #função para output de acordo com percentagem
  if percentagem <= 50 or nome == "Makima":
    print(f'Beleza {nome}!! Essa é uma boa pretendente!')
    percentagem_baixa.append(nome)
    num_baixa.append(percentagem)
  else:
    print(f'{nome}, mais uma que so quer o coraçao do chainsaw man, quando que alguem vai querer o meu coraçao!?!?')
    percentagem_alta.append(nome)

def lista_favoravel(): #função para output de acordo com lista totalmente favorável
  for menina in range(0, len(percentagem_baixa)):
    print(f'nome: {percentagem_baixa[menina]} - chances de morrer: {num_baixa[menina]}%')

while nome != "cabo":
  nome = input()
  
  if nome != "cabo":
    res = resultado(nome)
    
    if len(nome) <= 7:
      probabilidade(res, nome)

else:
  if len(percentagem_alta) >= len(percentagem_baixa):
    print('Desculpa pochita acho que nao vai ser hoje que voce vai poder ver meus sonhos')
  else:
    print('Epa ai sim! E hoje pochita!!')
  
  if len(percentagem_alta) == 0:
    lista_favoravel()