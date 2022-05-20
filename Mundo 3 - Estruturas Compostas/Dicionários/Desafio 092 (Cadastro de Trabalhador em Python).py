from datetime import date
cadastro = {}
nome = str(input('Nome: ')).strip().capitalize()
cadastro['Nome'] = nome
nasc = int(input('Ano de Nascimento: '))
atual = date.today().year
idade = atual - nasc
cadastro['Idade'] = idade
carteira = int(input('Carteira de Trabalho [0 se não tiver]: '))
if carteira != 0:
    cadastro['CTPS'] = carteira
    contr = int(input('Ano de contratação: '))
    cadastro['Contratação'] = contr
    salario = float(input('Salário: '))
    cadastro['Salário'] = salario
    cadastro['Aposentadoria'] = cadastro['Idade'] + ((cadastro['Contratação'] + 35) - atual)
elif carteira == 0:
    cadastro['CTPS'] = carteira
print(50 * '=')
for v, k in cadastro.items():
    print(f'{v} tem o valor {k}')