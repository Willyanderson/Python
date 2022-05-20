n1 = float(input('Digite sua nota: '))
n2 = float(input('Digite sua outra nota: '))
media = (n1 + n2) / 2
print('Sua Média é de {:.1f}!'.format(media))
if media < 5.0:
    print('\033[1;31mREPROVADO!\033[m')
elif 5.0 <= media <= 6.9:
    print('\033[1;33mRECUPERAÇÃO!\033[m')
elif media >= 7.0:
    print('\033[1;32mAPROVADO!\033[m')