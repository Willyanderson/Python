lista = []
listagem = []
while True:
    nome = str(input('Nome: ')).strip().capitalize()
    lista.append(nome)
    n1 = float(input('Nota 1: '))
    lista.append(n1)
    n2 = float(input('Nota 2: '))
    lista.append(n2)
    media = (n1 + n2) / 2
    lista.append(media)
    listagem.append(lista[:])
    lista.clear()
    resp = str(input('Quer continuar [S/N]? ')).strip().upper()
    if resp == 'N':
        break
print(30 * '=')
print('{:<4} {:<10} {:>9}'.format('Nº', 'NOME', 'MÉDIA'))
print(30 * '=')
for i, c in enumerate(listagem):
    print(f'{i:<4} {c[0]:<10} {c[3]:>8}')
print(50 * '=')
while True:
    notas = int(input('Mostrar notas de qual aluno [999 interrompe]? '))
    for a, n in enumerate(listagem):
        if notas == a:
            print(f'Notas de {n[0]} são: {n[1:3]}')
    print(50 * '=')
    if notas == 999:
        break
print('{:-^50}'.format(' FIM '))