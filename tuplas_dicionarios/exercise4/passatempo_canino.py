def vaquinha(ene_max, ene_dog, ene_gasta, adicional):
    print('Brinquedo da vaquinha! Vou chacoalhar')
    energia_perdida = ene_gasta + min(int(adicional), ene_dog) #adiciona perdas por chacoalhadas e previne a quantidade de perdas de ultrapassar o zero na subtração da energia do dog
    energia_atual = max(0, (ene_dog - int(adicional))) #subtrai as perdas da energia do doguinho e previne que energia não se torne menos que zero
    return energia_atual, energia_perdida

def chupeta(ene_max, ene_dog, ene_gasta, adicional):
    print('Minha pipeta! Vou morder')
    mordidas = int(adicional) #número de mordidas
    energia_5 = ene_dog - 5 #energia atual menos 5 
    energia_atual = min(ene_max, max(mordidas, energia_5)) #compara as mordidas e energia - 5 para saber quem é a maior e depois confere se é menor que o valor máximo de energia do doguinho
    energia_perdida = max(ene_gasta, (ene_gasta + (ene_dog - energia_atual))) #acrescenta perdas (se houver)
    return energia_atual, energia_perdida

def zegotinha(ene_max, ene_dog, ene_gasta, adicional):
    print('Meu preferido! Faz barulho e mordo')
    apertos = max(1, int(adicional)) #apertos para divisão da energia
    energia_atual = ene_dog//apertos #divisão da energia
    energia_perdida = ene_gasta + (ene_dog - energia_atual) #acrescenta perdas (se houver)
    return energia_atual, energia_perdida

def bolinha(ene_max, ene_dog, ene_gasta, adicional):
    print('ZOOOOOOOOOOOOOOOOOM')
    energia_perdida = ene_gasta + min(int(adicional)//4, ene_dog) #acrescenta perdas e previne a quantidade de perdas de ultrapassar o zero na subtração da energia do dog
    energia_atual = ene_dog - max(0, int(adicional)//4)  #tira perdas e previne que energia não se torne menos que zero
    return energia_atual, energia_perdida

def osso(ene_max, ene_dog, ene_gasta, adicional):
    print('Pausa para roer')
    energia_perdida = ene_gasta #a pausa não causa perdas
    energia_atual = min(ene_max, (ene_dog + (int(adicional)*2))) #coloca limite de máxima energia para o ganho de energia
    return energia_atual, energia_perdida

def comida(ene_max, ene_dog, ene_gasta, adicional):
    print(f'Uhh, {adicional} deve ser comestível')

    def par(cont):
        energia_perdida = ene_gasta
        comidinha = ene_dog + cont
        energia_atual = min(ene_max, comidinha)
        return energia_atual, energia_perdida

    def impar(cont):
        energia_perdida = ene_gasta + min(cont, ene_dog)
        energia_atual = max(0, ene_dog - cont)
        return energia_atual, energia_perdida

    cont = len(adicional)
    imp_par = [par(cont), impar(cont)]
    energia_atual, energia_perdida = imp_par[cont % 2] #resto define chamada de função par ou impar
    return energia_atual, energia_perdida

dic_brincadeiras = { #define objetos para chamar as funções de cada caso
    'Vaquinha': vaquinha,
    'Chupeta': chupeta,
    'Zé Gotinha': zegotinha,
    'Bolinha': bolinha,
    'Osso': osso,
    'Comida': comida,
}

energia_doguinho = int(input()) #define valor max sempre a ser comparado
energia_gasta = 0 #define energias gastas
energia = energia_doguinho #faz alteração na energia do doguinho

while energia > 0 and energia_gasta < 100: # define os limites para parar o recebimento de inputs
    obj_info = input() 
    lista_obj_info = obj_info.split(': ')
    obj = lista_obj_info[0]
    info = lista_obj_info[1]
    energia, energia_gasta = dic_brincadeiras[obj](energia_doguinho, energia, energia_gasta, info) #faz loop de ações de brincadeiras

energia_gasta = min(100, energia_gasta) #previne que o máximo de energia gasta seja 100
n_energia_gasta = energia_gasta//10
n = 'a' * max(1, n_energia_gasta)
print(f'Mamãe chegou! Gastei {int(energia_gasta)} pontos da minha energia e estou c{n}nsada, mas vou correr para seus braços!')