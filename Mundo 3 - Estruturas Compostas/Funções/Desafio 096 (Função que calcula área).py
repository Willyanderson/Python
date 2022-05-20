def lin():
    print(25* '=')

def area(l, c):
    a = l * c
    print(f'A área de um terreno {l:.1f}x{c:.1f} é de {a:.1f}m².')

lin()
print('{:^25}'.format('CONTROLE DE TERRENO'))
lin()
l = float(input('Largura (em m): '))
c = float(input('Comprimento (em m): '))
area(l, c)