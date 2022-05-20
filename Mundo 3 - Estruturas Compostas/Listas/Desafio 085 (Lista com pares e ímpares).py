lista = []
pares = []
impares = []
for c in range(0, 7):
    lista.append(int(input(f'Digite o {c+1}º valor: ')))
    for v in lista:
        if v % 2 == 0:
            pares.append(v)
        else:
            impares.append(v)
    lista.clear()
print(17 * '=-=')
pares.sort(reverse=True)
impares.sort(reverse=True)
print(f'Os valore pares digitados foram: {pares}')
print(f'Os valores ímpares digitados foram: {impares}')