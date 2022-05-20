matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
par = s3c = maiorl2 = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
        if matriz[l][c] % 2 == 0:
            par += matriz[l][c]
        if c == 2:
            s3c += matriz[l][c]
print(15 * '=-=')
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end = '')
    print()
print(15 * '=-=')
print(f'A soma dos valores pares é {par}.')
print(f'A soma dos valores da terceira coluna é {s3c}.')
for c in range(0, 3):
    if c == 0:
        maiorl2 = matriz[1][c]
    elif matriz[1][c] > maiorl2:
        maiorl2 = matriz[1][c]
print(f'O maior valor da segunda coluna é {maiorl2}')
