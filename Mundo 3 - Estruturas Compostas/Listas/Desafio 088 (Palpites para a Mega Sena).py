from random import randint
from time import sleep
print(17 * '=-=')
print('{:^51}'.format('MEGA SENA'))
print(17 * '=-=')
jogos = []
lista = []
quant = int(input('Quantos jogos você quer que eu sorteie? '))
print()
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break        
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('{:=^51}'.format(f' SORTEANDO {quant} JOGOS '))
print()
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(1)
print()
print('{:=^51}'.format(' BOA SORTE '))