from random import randint
from time import sleep
numeros = []
def sorteia(lista):    
    print('Sorteando 5 valores da lista: ', end='')
    for c in range(0, 5):
        lista.append(randint(1, 10))
    for i, v in enumerate(lista):
        print(f'{v}', end = ' ', flush=True)
        sleep(0.5)
    print('FIM!')

def somaPar(lista):
    s = 0
    for i, v in enumerate(lista):
        if v % 2 == 0:
            s += v
    print(f'Somando os valores pares de {lista}, temos {s}.')

sorteia(numeros)
somaPar(numeros)