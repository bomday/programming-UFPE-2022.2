pets_inimigos = {
  'cachorro': ['gato'],
  'hamster': ['cachorro', 'gato'],
  'gato': ['cachorro', 'peixe', 'hamster'],
  'peixe': ['gato']
}

pets_necessidades = {
  'cachorro': ['coleira', 'ração', 'ursinho de pelúcia'],
  'hamster': ['ração', 'roda para hamster', 'serragem'],
  'gato': ['bola de lã', 'caixa de areia', 'ração', 'ratinho de brinquedo'],
  'peixe': ['aquário', 'filtro', 'ração']
}

consulta_pets = input()
lista_consulta = consulta_pets.split(' e ')
nasceu = input()
pet_impossivel = False
pet_inimigo = False
lista_pet_impossivel = []

for pet in range(0, len(lista_consulta)): #consulta pets podem ser adotados
    if lista_consulta[pet] not in pets_necessidades:
        pet_impossivel = True
        lista_pet_impossivel.append(lista_consulta[pet])
        
def pet_inimigomigos(lista_ini, pet, pet_inimigo, lista_geral): #consulta pets inimigos
    for animal in lista_geral:
        if animal in lista_ini[lista_geral[pet]]:
            pet_inimigo = True
            print(f'Sérgio, o(a) {lista_geral[pet]} tem o(a) {animal} como inimigo. Não é possível adotá-los juntos, a não ser que sejam recém nascidos')       
    
    return pet_inimigo

if pet_impossivel == False and nasceu == 'sim': #consulta se pets serão adotados
    print('Como os animais são recém nascidos, eles podem ser adotados juntos!')
elif pet_impossivel == False and nasceu != 'sim':
    for pet in range(0, len(lista_consulta)): 
        pet_inimigo = pet_inimigomigos(pets_inimigos, pet, pet_inimigo, lista_consulta)
else:
    for bicho in lista_pet_impossivel:
        print(f'Sérgio, o animal {bicho} não estava nas suas potenciais escolhas, logo ele não pode ser analisado.')

if pet_inimigo == False and pet_impossivel == False: #outputs para pets que serão adotados
    print('Segue aqui as necessidades dos animais:')
    for pet in lista_consulta:
        print(f'As necessidades do(a) {pet} são:')
        for necessidade in pets_necessidades[pet]:
            print(f'- {necessidade};')
    print('Dito isso, vamos adotá-los!!!')