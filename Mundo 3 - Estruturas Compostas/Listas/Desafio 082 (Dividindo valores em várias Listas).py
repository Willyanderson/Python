lista = []
pares = []
impares = []
while True:
    valor = int(input('Digite um valor: '))
    lista.append(valor)
    if valor % 2 == 0:
        pares.append(valor)
    elif valor % 2 == 1:
        impares.append(valor)
    sn = str(input('Quer continuar [S/N]? ')).strip().upper()
    if sn in 'N':
        break
lista.sort()
pares.sort()
impares.sort()
print(52 * '=')
print(f'Todos os valores digitados: {lista}')
print(f'Valores que são pares: {pares}')
print(f'Valores que são ímpares: {impares}')
print(52 * '=')