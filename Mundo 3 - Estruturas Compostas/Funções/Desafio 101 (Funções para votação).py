from datetime import date
def voto(anonasceu):
    global ano
    atual = date.today().year
    idade = atual - ano
    if idade < 18:
        return print(f'Com {idade}: NÃO VOTA.')
    if 18 < idade < 65:
        return print(f'Com {idade}: VOTO OBRIGATÓRIO.')
    if idade > 65:
        return print(f'Com {idade}: VOTO OPCIONAL.')


ano = int(input('Em que ano você nasceu? '))
voto(ano)
