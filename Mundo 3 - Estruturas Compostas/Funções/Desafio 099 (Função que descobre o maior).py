from time import sleep
def lin():
    print(19 * '=-=')

def maior(*num):
    cont = maior = 0
    print('Analizando os valores passados...')
    sleep(1)
    for v in num:
        print(f'{v}', end = ' ', flush=True)
        sleep(0.5)
        if cont == 0:
            maior = v
        else:
            if v > maior:
                maior = v
        cont += 1
    print(f'Foram informados {len(num)} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')
    
lin()    
maior(2, 9, 4, 5, 7, 1)
lin()
maior(4, 7, 8)
lin()
maior(1, 2)
lin()
maior(6)
lin()
maior()
lin()