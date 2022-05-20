n = int(input('Me diga um número: '))
resultado = n % 2 #Se o resto da divisão(%) do número for 1 é pq ele é ÍMPAR e se for 0 ele é PAR
if resultado == 0:
    print('{} é PAR!'.format(n))
else:
    print('{} é ÍMPAR!'.format(n))