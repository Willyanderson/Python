print(51 * '=')
dados = {}
gols = []
listagem = []
while True:
    j = str(input('Nome do Jogador: ')).strip().capitalize()
    dados['Nome'] = j
    partidas = int(input(f'Quantas partidas {j} jogou? '))
    for p in range(0, partidas):
        gols.append(int(input(f'Quantos gols {j} fez na {p+1}ª partida: ')))
    dados['Gols'] = gols[:]
    dados['Total'] = sum(gols)
    gols.clear()
    listagem.append(dados.copy())
    resp = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
    if resp == 'N':
        break
    print(51 * '=')
print(17 * '=-=')
print(f'{"Co"}  {"Nome"}           {"Gols"}          {"Total"}')
print(51 * '=')
for i, v in enumerate(listagem):
    print(f'{i:<0}   ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print(51 * '=')
while True:
    busca = int(input('mostrar dados de qual jogador [999 paraparar]? '))
    if busca >= len(listagem):
        print(f'ERRO! Não existe jogador com código {busca}!')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {listagem[busca]["Nome"]}:')
        for i, g in enumerate(listagem[busca]['Gols']):
            print(f'      No {i+1}º jogo fez {g} gols')
    if busca == 999:
        break
    print(51 * '=')
print('{:=^51}'.format(' VOLTE SEMPRE '))