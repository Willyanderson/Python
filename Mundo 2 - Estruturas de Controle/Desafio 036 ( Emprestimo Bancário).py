valor = float(input('Qual o valor da casa: R$'))
salario = float(input('Qual o sálario do comprador: R$'))
anos = int(input('Em quantos anos o comprador pretende pagar: '))
c1 = valor / (anos * 12)
c3 = salario * 0.3
print()
print('Você terá que pagar R${:.2f} reais por mês em {} anos até\ncompletar o valor de R${:.2f} reias, que é o valor da casa.'.format(c1, anos, valor))
if c1 <= c3:
    print()
    print('Você poderá comprar essa casa, já que sua prestação custará R${:.2f} reais,\nnão excedendo os 30% de seu salário que é de R${:.2f} reais.'.format(c1, c3))
else:
    print()
    print('Empréstimo NEGADO!')