pessoas = []
dados = []
maiorp = menorp = 0
while True:
    dados.append(str(input('Nome: ')).strip().capitalize())
    dados.append(int(input('Peso: ')))
    if len(pessoas) == 0:
        maiorp = menorp = dados[1]
    else:
        if dados[1] > maiorp:
            maiorp = dados[1]
        if dados[1] < menorp:
            menorp = dados[1]
    pessoas.append(dados[:])    
    dados.clear()
    resp = str(input('Quer continuar [S/N]? ')).strip().upper()
    if resp == 'N':
        break
print(12 * '=-=')
print(f'Foram cadastradas {len(pessoas)} pessoas!')
print(f'O maior peso foi de {maiorp:.1f}Kg. Peso de', end =' ')
for p in pessoas:
    if p[1] == maiorp:
        print(f'{p[0]}', end = ' ')
print(f'O menor peso foi de {menorp:.1f}Kg. Peso de', end = ' ')
for p in pessoas:
    if p[1] == menorp:
        print(f'{p[0]}', end = ' ')
