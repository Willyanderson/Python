from random import randint
from time import sleep
escolhido = randint(0, 5) #Faz o computador "PENSAR"
print('{:^55}'.format('──────────────────────────╮•╭───────────────────────────'))
print('\033[1;34m  Vou pensar em um número entre 0 e 5. Tente advinhar!  \033[m')
print('──' * 28)
jogador = int(input('\033[1;30mEm que número eu pensei? \033[m'))
print('\033[32mPROCESSANDO...\033[m')
sleep(2) #Faz o computador esperar 2 seg.
if jogador == escolhido:
    print('\033[1;32mParabéns!! {} foi exatamente o número que pensei!\033[m'.format(escolhido))
else:
    print('\033[1;31mHA-HA Ganhei! Eu pensei no número {} em vez do número {}!\nMais sorte da próxima vez...\033[m'.format(escolhido, jogador))