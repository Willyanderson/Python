print(19 * '=',' Super Gerador de PA ', 19 * '=')
primeiro = int(input('Primeiro Termo: '))
razao = int(input('Razão da PA: '))
print()
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais   
    while cont <= total:
        print('{} ➝ '.format(termo), end = ' ')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('Progressão finalizada com {} termos mostrados'.format(total))