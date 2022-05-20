lista = []
while True:
    v = int(input('Digite um valor: '))
    if v not in lista:
        lista.append(v)    
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não irei adicionar...')
    sn = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
    if sn == 'N':
        break
print(35 * '=')
lista.sort()
print(f'Os valores digitados foram: {lista}')