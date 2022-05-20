from random import randint
print(21 * '=-=')
print('{:^63}'.format('PAR OU ÍMPAR'))
print(21 * '=-=')
v = 0
while True:
    jogador = int(input('Digite um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou ímpar (P/I)? ')).strip().upper()[0]   
    print(63 * '=')
    print(f'   Você jogou {jogador} e o computador jogou {computador}. Total de {total},', end = ' ')
    print('DEU PAR!  ' if total % 2 == 0 else 'DEU ÍMPAR!  ')
    print(63 * '=')
    if tipo == 'P':  
        if total % 2 == 0:
            print('{:^63}'.format('Você GANHOU, PARABÉNS!!'))
            v += 1
        else:
            print('{:^63}'.format('Você PERDEU!'))
            print(21 * '=-=')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('{:^63}'.format('Você GANHOU, PARABÉNS!!'))
            v += 1
        else:
            print('{:^63}'.format('Você PERDEU!'))
            print(21 * '=-=')
            break
    print('Vamos jogar novamente...')
    print(21 * '=-=')
print('{:^63}'.format(f'GAME OVER! Você venceu {v} vezes.'))
print(21 * '=-=')