from random import randint
from time import sleep
from operator import itemgetter
jogo = {}
ranking = dict()
contagem = [1, 2, 3, 4, 5]
print('Valores Sorteados:')
for c in range(1, 5):
    dado = randint(1, 6)
    jogo[f'Jogador{c}'] = dado
    print(f'     O Jogador{c} tirou {dado} no dado.')
    sleep(1)
print(18 * '==')
print('    =-= RANKING DOS JOGADORES =-=')
ranking = sorted(jogo.items(), key = itemgetter(1), reverse = True)
for i, v in enumerate(ranking):
    print(f'      {i+1}º lugar: {v[0]} com {v[1]}')
    sleep(1)
print(18 * '==')