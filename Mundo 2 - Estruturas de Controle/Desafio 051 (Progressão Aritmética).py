print(50 * '=')
print('{:^50}'.format(' 10 TERMOS DE UMA PA '))
print(50 * '=')
pt = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
a10 = pt + (9 * razão) #formula matématico para encontrar o 10 termo de uma PA
for c in range(pt, a10 + razão, razão):
    print(c, end=' → ')
print('ACABOU', end='')