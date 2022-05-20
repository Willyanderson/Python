matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
#lista = [[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]]
for l in range(0, 3):  
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: ')) 
print(17 * '=-=')
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end = '')
    print()