num = (int(input('Digite um valor: ')), int(input('Digite outro valor: ')),
int(input('Digite mais um valor: ')), int(input('Digite um último valor: ')))
print(45 * '=')
print(f'Valores digitados: {num}')
print(45 * '=')
if num.count(9) == 1:
    print(f'O número 9 foi digitado {num.count(9)} vez!')
else:
    print(f'O número 9 foi digitado {num.count(9)} vezes!')
if 3 in num:
    print(f'O primeiro valor 3 apareceu na {num.index(3)+1}ª posição!')
else: 
    print('O valor 3 não foi digitado em nenhuma posição!')
print(f'Os valores pares digitados: ', end = '')
for n in num:
    if n % 2 == 0:
        print(n, end = ' ')