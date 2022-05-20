import random
a1 = input('Nome do primeiro aluno: ')
a2 = input('Nome do segundo aluno: ')
a3 = input('Nome do terceiro aluno: ')
a4 = input('Nome do quarto aluno: ')
print('O aluno escolhido para apagar o quadro hoje foi {}! Parabéns, pode começar pequeno gafanhoto!'.format(random.choice([a1, a2, a3, a4])))