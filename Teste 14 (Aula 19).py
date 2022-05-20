#DICIONÁRIOS
#pessoas = {'nome': 'Willy', 'idade': 18, 'sexo': 'M'}
#print(pessoas['nome'])

#print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
#Dentro de ' ' usa-se " ".

'''Valores, Chaves e Itens:
#Valores:
print(pessoas.values())
#Chaves:
print(pessoas.keys())
#Itens:
print(pessoas.items())'''

#Apagando elementos:
#del pessoas['sexo']

#Substituindo elementos:
#pessoas['nome'] = 'Gustavo'

#Adicionando elementos: (Não Precisa do .append())
#pessoas['time'] = 'Flamengo'

#Usando uma Estrutura de Repetição (for e while):
#for k in pessoas.keys():
#    print(k)
#for k, v in pessoas.items():
#    print(f'{k}: {v}')

#Dicionários dentro de lista:
'''brasil = []
estado1 = {'uf': 'Rio Grande do Norte', 'sigla': 'RN'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil[0]['uf'])'''

estado = dict()
brasil = []
for c in range(0, 2):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla: '))
    brasil.append(estado.copy())
for e in brasil:
        print(f'{e["uf"]}, {e["sigla"]}')
#   for v in e.values():
#        print(v, end = ' ')
 #   print()