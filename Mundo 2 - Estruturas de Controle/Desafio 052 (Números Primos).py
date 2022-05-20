num = int(input('Digite um número: '))
cont = 0
for c in range(1, num+1):
    if num % c == 0: #Saber se é primo(divisível por 1 ou ele mesmo)
        print('\033[1;31m', end='')
        cont += 1
    else:
        print('\033[m', end='')
    print('{}'.format(c), end=' ')
print('\n\033[mO número {} foi divisível {:.0f} vezes!'.format(num, cont))
if cont == 2:
    print('E por isso ele É PRIMO!')
else:
    print('E por isso ele NÃO É PRIMO!')