p = float(input('Preço do produto: '))
c = p - (p * (5/100))
print('O produto terá o preço de R${:.2f} se usado os 5% de desconto!'.format(c))