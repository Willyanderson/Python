ano = int(input('Digite seu ano de nascimento: '))
c1 = 2022 - ano
print('Você tem {} anos, lhe colocando na categoria:'.format(c1))
if c1 <= 9:
    print('\033[1;34mMIRIM\033[m')
elif 10 <= c1 <= 14:
    print('\033[1;34mINFANTIL\033[m')
elif 15 <= c1 <= 19:
    print('\033[1;34mJUNIOR\033[m')
elif 20 <= c1 <= 25:
    print('\033[1;34mSÊNIOR\033[m')
else: 
    print('\033[1;34mMASTER\033[m')