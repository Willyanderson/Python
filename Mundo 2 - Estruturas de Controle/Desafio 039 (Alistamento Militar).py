ano = int(input('Digite seu ano de nascimento: '))
c1 = 2022 - ano
c2 = 18 - c1
c3 = c2 + 2022
c4 = ano + 18
if c1 < 18:
    print('Você tem {} anos no ano atual de 2022.\nFaltando {} anos para o seu alistamento, que será em {}!'.format(c1, c2, c3))
elif c1 == 18:
    print('Você tem {} anos no ano atual de 2022.\nIsso indica que ja é hora de se alistar!'.format(c1))
elif c1 > 18:
    print('Você tem {} anos no ano atual de 2022.\nIsso indica que já passou do tempo de seu alistamento que deveria ocorrer em {}!'.format(c1, c4))