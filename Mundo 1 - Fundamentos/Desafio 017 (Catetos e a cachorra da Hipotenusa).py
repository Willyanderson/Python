from math import hypot
x = float(input('Digite a medida do cateto adjacente: '))
y = float(input('Digite a medida do cateto oposto: '))
hi = hypot(x, y)
print('O comprimento da hipotenusa desse trângulo retângulo é: {}'.format(hi))