n = int(input('Digite um número: '))
print()
print('\033[1;34m{}\033[m: para binário\n\033[1;32m{}\033[m: para octal\n\033[1;33m{}\033[m: para hexadecimal'.format('1','2','3'))
print()
escolha = int(input('Escolha qual será a base de converão: '))
if escolha == 1:
    print('\033[1;34mBinário\033[m: {}'.format(bin(n)[2:])) #O "[2:]" serve para o fatiamento do número que aparecerá da 2 casa adiante
elif escolha == 2:
    print('\033[1;32mOctal\033[m: {}'.format(oct(n)[2:]))
elif escolha == 3:
    print('\033[1;33mHexadecimal\033[m: {}'.format(hex(n)[2:]))