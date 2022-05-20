print(22 * '=', ' Gerador De PA ', 22 * '=')
primeiro = int(input('Primeiro Termo: '))
razao = int(input('Razão da PA: '))
print()
termo = primeiro
cont = 1
while cont <= 10:
    print('{} ➝ '.format(termo), end = ' ')
    termo += razao
    cont += 1
print('PAUSA')