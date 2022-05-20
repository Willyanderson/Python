#print('\033[4;30;46mOlá mundo!')
#print('\033[7;33;44mOlá Mundo!\033[m')

#n1 = input('Digite um número: ')
#n2 = input('Digite outro número: ')
#print('Os valores são:\n\033[1;34;43m{}\033[m e \033[4;31m{}\033[m!'.format(n1, n2))

#nome = input('Qual é o seu nome? ')
#print('Olá! Prazer em te conhecer, {}{}{}!!!'.format('\033[1;36m', nome, '\033[m'))

nome = (input('Qual é o seu nome? '))
cores = {'limpa':'\033[m', 'azul':'\033[34m', 'vermelho':'\033[31m', 'pretoebranco':'\033[7;30m'} #Exemplo de Dicionário
print('Olá! Prazer em te conhecer, {}{}{}!!!'.format(cores['azul'], nome, cores['limpa'] ))