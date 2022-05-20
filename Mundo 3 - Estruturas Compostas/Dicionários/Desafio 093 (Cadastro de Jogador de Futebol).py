est = {}
total = 0
gol = []
jogador = str(input('Nome do jogador: ')).strip().capitalize()
est['nome'] = jogador
partidas = int(input(f'Quantas partidas {jogador} jogou? '))
for g in range(0, partidas):
    gols = int(input(f'Quantos gols {jogador} fez na {g+1}ª partida? '))
    gol.append(gols)
    est['gols'] = gol
    total += gols
    est['total'] = total    
print(17 * '=-=')
for v, k in est.items():
    print(f'O campo {v} tem o valor {k}.')
print(17 * '=-=')
print(f'O jogador {jogador} jogou {partidas} partidas.')
for i, v in enumerate(gol):
    print(f'    => Na {i+1}ª partida, {jogador} fez {v} gols.')
print(f'Foi um total de {total} gols.')