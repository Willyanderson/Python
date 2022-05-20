from random import randint
print('=============== ADVINHAÇÃO ===============')
print('Vou pensar em um número entre 0 e 10,\nTente adivinhar...')
print()
escolhido = randint(0, 10)
tentativas = 1
num = int(input('Qual seu palpite: '))
while num != escolhido:
    if num > escolhido:
        print('Menos... Tente mais uma vez.')
    if num < escolhido:
        print('Mais... Tente mais uma vez.')
    num = int(input('Qual seu palpite: '))
    tentativas += 1
print()
print('Parabéns!! {} foi o número que pensei!\nForam necessários {} palpites até o acerto.'.format(escolhido, tentativas))
print('==========================================')
