string = input()
lista_string = [letra for letra in string]
cont = len(lista_string) - 1
frase_final = ''

def frase(lista, cont, frase_formada):
  if cont == 0:
    frase_formada = frase_formada + lista[cont]
    return frase_formada
  else:
    if cont == (len(lista) - 1):
      frase_formada = lista[cont]
    else:
      frase_formada = frase_formada + lista[cont]
    
    cont -= 1
    return frase(lista, cont, frase_formada)

frase_final = frase(lista_string, cont, frase_final)
print(frase_final)