n = 0
cont = 0
soma = 0
while n != 999:
    n = int(input('Digite um número (999 para parar): '))
    cont += 1
    soma += n
c = cont - 1
s = soma - 999
print('Você digitou {} números e a soma entre eles foi {}'.format(c, s))