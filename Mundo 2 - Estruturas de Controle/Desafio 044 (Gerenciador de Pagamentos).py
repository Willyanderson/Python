print('{:=^30}'.format(' LOJAS WILLY '))
preço = float(input('Preço das compras: R$'))
print('FORMAS DE PAGAMENTO')
print('1: à vista dinheiro/cheque\n2: à vista cartão\n3: 2x no cartão\n4: 3x ou mais no cartão')
escolha = int(input('Qual é a opção? '))
if escolha == 1:
    print('Sua compra custará R${:.2f} reais.'.format(preço - (preço * 0.1)))
elif escolha == 2:
    print('Sua compra custará R${:.2f} reais.'.format(preço - (preço * 0.05)))
elif escolha == 3:
    print('Sua compra será parcelada em 2x de R${:.2f} reais SEM JUROS.'.format(preço / 2))
elif escolha == 4:
    pp = preço / parcelas
    parcelas = int(input('Quantidade de parcelas: '))
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS\nSua compra de R${:.2f} vai custar R${:.2f} no final.'.format(parcelas, pp + (pp * 0.2), preço,  parcelas * (pp + (pp * 0.2))))
else:
    print('OPÇÃO INVÁLIDA de pagamento, tente novamente!')