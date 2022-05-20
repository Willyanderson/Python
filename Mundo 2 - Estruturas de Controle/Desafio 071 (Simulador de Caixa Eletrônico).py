print(13 * '=-=')
print('{:^39}'.format('CAIXA ELETRÔNICO'))
print(13 * '=-=')
saque = int(input('Valor do saque: R$'))
total = saque
cinquenta = total // 50
vinte = (total - (cinquenta * 50)) // 20
dez = (total - ((cinquenta * 50) + (vinte * 20))) // 10
um = (total - ((cinquenta * 50) + (vinte * 20) + (dez * 10))) // 1
print(f'Total de {cinquenta} cédulas de R$50')
print(f'Total de {vinte} cédulas de R$20')
print(f'Total de {dez} cédulas de R$10')
print(f'Total de {um} cédulas de R$1')
print(13 * '=-=')
print('{:^39}'.format('VOLTE SEMPRE!'))
print(13 * '=-=')