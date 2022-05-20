cont = h = m20 = 0
while True:
    print(41 * '=')
    print('{:^41}'.format('CADASTRE UMA PESSOA'))
    print(41 * '=')
    idade = int(input('Idade: '))
    if idade > 18:
        cont += 1
    sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    if sexo == 'M':
        h += 1
    elif idade < 20 and sexo =='F':
        m20 += 1 
    continua = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
    if continua == 'N':
        break
print(41 * '=')
print(f' Total de pessoas com mais de 18 anos: {cont}')
if h == 1:    
    print(' Ao todo, temos 1 homem cadastrado.')
else:
    print(f' Ao todo temos {h} homens cadastrados.')
if m20 == 1:
    print(f' E temos 1 mulher com menos de 20 anos.')
else:
    print(f' E temos {m20} mulheres com menos de 20 anos.')
print(41 * '=')