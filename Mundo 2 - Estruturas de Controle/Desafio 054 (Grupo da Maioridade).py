from datetime import date
atual = date.today().year
cont = 0
totalmaior = 0
totalmenor = 0
for c in range(0, 7):
    cont += 1
    ano = int(input('Em que ano a {}ª pessoa nasceu: '.format(cont)))
    idade = atual - ano
    if idade >= 18:
       totalmaior += 1 
    else:
        totalmenor += 1
print('Ao todo tivemos {} pessoas maiores de idade'.format(totalmaior))
print('E também tivemos {} pessoas menores de idade'.format(totalmenor))