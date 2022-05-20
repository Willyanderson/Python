soma = 0
maioridadehomem = 0
nomemaisvelho = ''
mulhermenos20 = 0
for c in range(1, 5):
    print('========== {}ª PESSOA =========='.format(c))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo (M/F): ')).strip().upper()
    soma += idade
    if c == 1 and sexo == 'M':
        maioridadehomem = idade
        nomemaisvelho = nome
    if sexo == 'M' and idade > maioridadehomem:
        maioridadehomem = idade
        nomemaisvelho = nome
    if sexo == 'F' and idade < 20:
        mulhermenos20 += 1
media = soma / 4
print()
print('A média de idade desse grupo de pessoas é de {:.0f} anos.'.format(media))
print('O homem mais velho se chama {} e ele tem {} anos.'.format(nomemaisvelho, maioridadehomem))
print('No grupo, há {} mulheres com menos de 20 anos.'.format(mulhermenos20))