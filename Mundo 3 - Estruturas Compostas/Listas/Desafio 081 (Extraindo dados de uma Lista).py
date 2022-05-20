lista = []
cont = 0
while True:
    valores = int(input('Digite um valor: '))
    lista.append(valores)
    if valores == 5:
        cont += 1
    sn = str(input('Quer continuar [S/N]: ')).strip().upper()
    if sn in 'N':
        break
lista.sort(reverse = True)
print(35 * '=')
print(f'Valores digitados em Ordem Decrescente: {lista}')
print(f'Foram digitados {len(lista)} valores!')
if cont >= 1:   
    print(f'O valor 5 foi faz parte da lista!')
else:
    print('O valor 5 não está na lista!')