maior = 0
menor = 0
for p in range(0, 5):
    peso = float(input('Qual é o peso da {}ª pessoa (em kg): '.format(p)))
    if p == 1: #se tiver apenas 1 valor ele será o maior e o menor peso
        maior = peso
        menor = peso
    else:
        if peso > maior: #se o peso lido for maior que o anterior ele será o maior
            maior = peso
        if peso < menor: #se o peso lido for menor que o  anterior ele será o menor
            menor = peso
print('O maior peso foi {:.1f}Kg\nE o menor foi {:.1f}Kg'.format(maior, menor))