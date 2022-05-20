aluno = {}
nome = str(input('Nome: ')).strip().capitalize()
aluno['Nome'] = nome
media = float(input('Média: '))
aluno['Média'] = media
if media >= 6:
    situaçao = 'Aprovado'
    aluno['Situação'] = situaçao
else:
    situaçao = 'Reprovado'
    aluno['Situação'] = situaçao
print(f'Nome é igual a {aluno["Nome"]}')
print(f'Média é igual a {aluno["Média"]:.1f}')
print(f'Situação é igual a {aluno["Situação"]}!')
