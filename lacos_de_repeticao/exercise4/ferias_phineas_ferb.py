invencao = input()
etapa = input()
total_etapas = 0
total_falhas = 0
despesa = 0
status = ''
status_incorreto = 0

while (etapa != 'desistir' and etapa != 'concluir' and status != 'desistir' and status != 'concluir'):
  if etapa != 'dar um plus':
    custo = int(input())
    tentativas = int(input())
    status = 'incorreto'
    
    while (tentativas > 0 and status == 'incorreto'):
      tentativas = tentativas - 1
      status = input()
      status_incorreto = status_incorreto + 1
      
      if status == 'incorreto':
        despesa = despesa + custo
        total_falhas = total_falhas + 1
        print(f'Ainda não consegui {etapa} corretamente, e essa tentativa me custou R${custo}')
      
    else: 
      if status == 'correto':
        despesa = despesa + custo
        total_etapas = total_etapas + 1
        print(f'Oba! consegui {etapa}, o que me custou R${custo}')
        print(f'ANDAMENTO DO PROJETO: Etapas realizadas - {total_etapas} ; Tentativas falhas - {total_falhas}')
        etapa = input()
      elif tentativas == 0 and status != 'desistir' and status != 'concluir':
        print(f'ANDAMENTO DO PROJETO: Etapas realizadas - {total_etapas} ; Tentativas falhas - {total_falhas}')
        etapa = input()
    
  else:
    custo = int(input())
    despesa = despesa + custo
    print(f'Agora o(a) {invencao} ficou ainda mais legal! Pena que precisei gastar R${custo}')
    etapa = input()

else:
  if etapa == 'desistir' or status == 'desistir':
    print(f'A jornada da construção do(a) {invencao} acaba aqui.')
    print(f'Infelizmente, o sonho do(a) {invencao} foi interrompido e levou junto com ele R${despesa}')
  else:
    print(f'A jornada da construção do(a) {invencao} acaba aqui.')
    print(f'Uhuuu, finalmente o(a) {invencao} tá pronto(a)! Esse projeto me custou R${despesa}')