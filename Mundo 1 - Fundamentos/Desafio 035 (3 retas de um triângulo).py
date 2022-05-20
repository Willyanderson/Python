r1 = float(input('Qual o comprimento do primeiro segmento? '))
r2 = float(input('Qual o comprimento do segundo segmento? '))
r3 = float(input('Qual o comprimento do terceiro segmento? '))
if r1 + r2 > r3 and r2 + r3 > r1 and r1 + r3 > r2:
    print('É possível formar um triângulo utilizando esses 3 segmentos!')
else:
    print('Não é possível formar um triangulo usando esses 3 segmentos!')