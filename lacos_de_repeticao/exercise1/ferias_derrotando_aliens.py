count = 0
message = input()

while ((message != 'O relógio descarregou!') and (message != 'Por hoje já deu')):
  count += 1
  message = input()
else:
  if message == 'O relógio descarregou!':
    print(f'Corra Ben! Você já derrotou {count} aliens')
  else: 
    print(f'Muito Ben Ben! hehe você derrotou {count} aliens hoje')