from random import randint
from time import sleep
itens = ('Pedra!','Papel!', 'Tesoura!')
pc = randint(0, 2)
print('{}'.format('*══════* JOKEMPÔ *══════*'))
print('Opções:')
print()
print('〚0〛Pedra\n〚1〛Papel\n〚2〛Tesoura')
print()
escolha = int(input('Qual sua jogada: '))
print('PEDRA')
sleep(1)
print('PAPEL')
sleep(1)
print('OU TESOURA')
print('*═══════════*═══════════*')
print('Computador jogou {}'.format(itens[pc]))
print('Você jogou {}'.format(itens[escolha]))
print('*═══════════*═══════════*')
if pc == 0 and escolha == 0:
    print('EMPATE!')
elif pc == 0 and escolha == 1:
    print('PARABÉNS!! VOCÊ GANHOU!')
elif pc == 0 and escolha == 2:
    print('COMPUTADOR GANHOU!')
elif pc == 1 and escolha == 0:
    print('COMPUTADOR GANHOU!')
elif pc == 1 and escolha == 1:
    print('EMPATE!')
elif pc == 1 and escolha == 2:
    print('PARABÉNS!! VOCÊ GANHOU!')
elif pc == 2 and escolha == 0:
    print('PARABÉNS!! VOCÊ GANHOU!')
elif pc == 2 and escolha == 1:
    print('COMPUTADOR GANHOU!')
else:
    print('EMPATE!')
print('*══════════***══════════*')