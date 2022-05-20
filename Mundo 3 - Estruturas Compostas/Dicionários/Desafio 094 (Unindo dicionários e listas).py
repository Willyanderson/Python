geral = []
dados = {}
total = 0
while True:
    nome = str(input('Nome: ')).strip().capitalize()
    dados['Nome'] = nome
    idade = int(input('Idade: '))
    dados['Idade'] = idade
    total += idade
    sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    dados['Sexo'] = sexo
    geral.append(dados.copy())
    resp = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
    if resp == 'N':
        break
print(50 * '=')
print(f'- Foram cadastradas {len(geral)} pessoas.')
media = total / len(geral)
print(f'- A média de idade do grupo é de {media:.0f} anos')
print(f'- As mulheres cadastradas foram:', end = ' ')
for e in geral:
    for v, k in e.items():
        if v == 'Sexo' and k == 'F':
            print(e['Nome'], end = ' ')
print('\n- Lista de pessoas que estão acima\nda média de idade:')
for p in geral:
    for v, k in p.items():
        if v == 'Idade' and k > media:
            print(f'{p["Nome"]} com {p["Idade"]} anos')
print('{:=^50}'.format(' FIM '))