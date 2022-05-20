print(15 * '=-=')
print('{:^45}'.format(' TABUADA '))
print(15 * '=-=')
print('Digite um número negativo parar PARAR')
while True:
    n = int(input('Quer ver a tabuada de qual valor: '))
    if n < 0:
        break
    print(45 * '=')
    for c in range(1, 11):
        m = n * c
        print(f'{n} x {c} = {m}')
    print(45 * '=')    
print(15 * '=-=')
print('{:^45}'.format(' Programa encerrado! Volte sempre '))
print(15 * '=-=')