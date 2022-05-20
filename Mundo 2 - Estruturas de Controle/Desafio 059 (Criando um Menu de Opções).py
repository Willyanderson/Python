from time import sleep
print('=========== Menu de Opções ===========')
print()
num1 = int(input('Primeiro valor: '))
num2 = int(input('Segundo valor: '))
opçao = 0
while opçao != 5:
    print()
    print('   (1) Somar\n   (2) Multiplicar\n   (3) Maior\n   (4) Novos números\n   (5) Sair do programa')
    print()
    opçao = int(input('====> Qual sua opção: '))
    soma = num1 + num2
    multiplicação = num1 * num2
    if opçao == 1:
        print('{} + {} = {}'.format(num1, num2, soma))
    elif opçao == 2:
        print('{} x {} = {}'.format(num1, num2, multiplicação))
    elif opçao == 3:
        if num1 > num2:
            print('{} é maior que {}'.format(num1, num2))
        elif num2 > num1:
            print('{} é maior que {}'.format(num2, num1))
        else:
            print('{} e {} são iguais'.format(num1, num2))
    elif opçao == 5:
        print('Encerrando o programa...')
        sleep(1)
        print('{:^39}'.format('PROGRAMA ENCERRADO!'))
    elif opçao == 4:
        print('Escolha 2 outros números:')
        num1 = int(input('Primeiro valor: '))
        num2 = int(input('Segundo valor: '))
        escolha = str(input('Esses são realmente seus 2 valores:[S/N] '))
        print()
        while escolha not in 'Ss':
            print('Escolha 2 outros números')
            num1 = int(input('Primeiro valor: '))
            num2 = int(input('Segundo valor: '))
            escolha = str(input('Esses são realmente seus 2 valores:[S/N] '))
        if escolha in 'Ss':
            print()
            print('   (1) Somar\n   (2) Multiplicar\n   (3) Maior\n   (4) Novos números\n   (5) Sair do programa')
            print()
            opçao = int(input('====> Qual sua opção: '))
            soma = num1 + num2
            multiplicação = num1 * num2
            if opçao == 1:
                print('{} + {} = {}'.format(num1, num2, soma))
            elif opçao == 2:
                print('{} x {} = {}'.format(num1, num2, multiplicação))
            elif opçao == 3:
                if num1 > num2:
                    print('{} é maior que {}'.format(num1, num2))
                elif num2 > num1:
                    print('{} é maior que {}'.format(num2, num1))
                else:
                    print('{} e {} são iguais'.format(num1, num2))
            elif opçao == 5:
                print('Encerrando o programa...')
                sleep(1)
                print('{:^39}'.format('PROGRAMA ENCERRADO!'))
    sleep(1)
    print(39 * '=')   