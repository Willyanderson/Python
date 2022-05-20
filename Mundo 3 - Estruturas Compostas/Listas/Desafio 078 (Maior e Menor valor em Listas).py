v = []
for cont in range(0, 5):
    v.append(int(input(f'Digite um valor para a posição {cont}: ')))
print(42 * '=')
print(f'Você digitou os valores: {v}')
print(f'O maior valor foi {max(v)}, estando nas posições ', end = '')
for i, valores in enumerate(v):
    if valores == max(v):
        print(f'{i}...', end = ' ')
print(f'\nO menor valor foi {min(v)}, estando nas posições ', end = '')
for i, valores in enumerate(v):
    if valores == min(v):
        print(f'{i}...', end = ' ')