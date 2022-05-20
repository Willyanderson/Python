cont = 0
cont1 = 0
maior = 0
menor = 9999999999999
num = int(input('Digite um número: '))
c = str(input('Quer continuar?[S/N] '))
while c not in 'Nn':
    n = int(input('Digite um número: '))
    c = str(input('Quer continuar?[S/N] '))
    cont1 += 1
    cont += n
    if n > maior:
       maior = n
    if n < menor:
        menor = n
con = cont1 + 1
soma = cont + num
media = soma / con
if num > maior:
    maior = num
if num < menor:
    menor = num
print('Você digitou {} números e a média foi {:.1f}'.format(con, media))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))