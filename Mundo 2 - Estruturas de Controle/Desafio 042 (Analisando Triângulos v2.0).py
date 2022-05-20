r1 = float(input('Qual o comprimento do primeiro segmento? '))
r2 = float(input('Qual o comprimento do segundo segmento? '))
r3 = float(input('Qual o comprimento do terceiro segmento? '))
if r1 + r2 > r3 and r2 + r3 > r1 and r1 + r3 > r2:
    print('Os segmentos acima PODEM FORMAR um triângulo ',end='') #Usa-se o ",end=''" para finalizar com um dos if abaixo
    if r1 != r2 and r1 != r3 and r2 != r3:
        print('ESCALENO!')
    elif r1 == r2 == r3:
        print('EQUILÁTERO!')
    else:
        print('ISÓSCELES!')
else:
    print('Não é possível formar um triangulo usando esses 3 segmentos!')