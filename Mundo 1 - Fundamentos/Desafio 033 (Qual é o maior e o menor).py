n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite mais um número: '))
if n1 > n2 and n1 > n3 and n2 > n3:
    print('O maior número é o {} e o menor é o {}!'.format(n1, n3)) 
elif n1 > n2 and n1 > n3 and n2 < n3:
    print('O maior número é o {} e o menor é o {}!'.format(n1, n2))
elif n1 < n2 and n1 < n3 and n2 > n3:
    print('O maior número é o {} e o menor é o {}!'.format(n2, n1))
elif n1 < n2 and n1 > n3 and n2 > n3:
    print('O maior número é o {} e o menor é o {}!'.format(n2, n3))
elif n1 < n2 and n1 < n3 and n2 < n3:
    print('O maior número é o {} e o menor é o {}!'.format(n3, n1))
elif n1 > n2 and n1 < n3 and n2 < n3:
    print('O maior número é o {} e o menor é o {}!'.format(n3, n2))
