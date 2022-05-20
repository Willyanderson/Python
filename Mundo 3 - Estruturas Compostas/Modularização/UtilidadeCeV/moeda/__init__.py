def moeda(n):
    n = f'R${n:.2f}'.replace('.', ',')
    return n


def metade(n, f=False):
    res = n / 2
    return res if f is False else moeda(res)


def dobro(n, f=False):
    res = n * 2
    return res if f is False else moeda(res)


def aumentar(n, p, f=False):
    res = n + (n * (p/100))
    return res if f is False else moeda(res)


def diminuir(n, p, f=False):
    res = n - (n * (p/100))
    return res if f is False else moeda(res)


def resumo(n, aum, dim):
    print(35 * '=')
    print('{:^35}'.format('RESUMO DO VALOR'))
    print(35 * '=')
    listagem = ('Preço analisado:', moeda(n),
    'Dobro do preço:', dobro(n, True),
    'Metade do preço:', metade(n, True),
    f'{aum}% de aumento:', aumentar(n, aum, True),
    f'{dim}% de redução:', diminuir(n, dim, True))
    for pos in range(0, len(listagem)):
        if pos % 2 == 0:
            print(f'{listagem[pos]:<25}', end = '')
        else:
            print(f'{listagem[pos]:>6}')
    print(35 * '=')