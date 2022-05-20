from time import sleep
def lin():
    print(13 * '=-=')

def contador(i, f, p):    
    print(f'Contagem de {i} até {f} de {p} em {p}:')
    sleep(2)
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont}', end=' ', flush=True)
            sleep(0.5) 
            cont += p
        print('FIM!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont}', end=' ', flush=True)
            sleep(0.5) 
            cont -= p
        print('FIM!')

lin()
contador(1, 10, 1)
lin()
contador(10, 0, 2)
lin()
print('Agora é sua vez:')
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
lin()
contador(i, f, p)
