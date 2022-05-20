l = []
for c in range (0, 5):
    v = int(input('Digite um valor: '))
    if c == 0 or v > l[-1]:
        l.append(v)
        print('Adcionado ao final da lista...')
    else:
        pos = 0
        while pos < len(l):
            if v <= l[pos]:
                l.insert(pos, v)
                print(f'Adicionado na posição {pos} da lista...')
                break
            pos += 1
print()
print(f'Os valores digitados em ordem foram: {l}')