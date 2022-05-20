#nome = str(input('Qual é seu nome? '))
#if nome =='Willy':
#    print('Que nome lindo você tem!')
#else:
#    print('Seu nome é legal!')
#print('Bom dia, {}'.format(nome))
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
m = (n1 + n2) / 2
print('A sua média foi {:.1f}!'.format(m))
if m >= 6.0:
    print('Suas notas estão boas, Parabéns!')
else:
    print('Suas notas estão abaixo da média, se esforce um pouco mais!')
