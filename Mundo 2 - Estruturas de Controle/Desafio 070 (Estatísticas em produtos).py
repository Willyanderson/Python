print(58 * '=')
print('{:^58}'.format('HIPERMERCADO'))
print(58 * '=')
total = totalmil = cont = menor = 0
barato = ''
while True:
    produto = str(input('Nome do Produto: '))
    preço = float(input('Preço: R$'))
    total += preço
    cont += 1
    if preço > 1000:
        totalmil += 1
    if cont == 1 or preço < menor:
        menor = preço
        barato = produto
    continua = str(input('Continuar [S/N]? ')).strip().upper()[0]
    if continua == 'N':
        break
print(58 * '=')
print(f'Preço total da compra: R${total:.2f} reais')
print(f'Total de produtos que custaram mais de R$1000,00 reias: {totalmil}')
print(f'O produto mais barato foi {barato} custando R${menor:.2f} reais')
print(58 * '=')
print('{:^58}'.format('OBRIGADO, VOLTE SEMPRE!'))
print(58 * '=')