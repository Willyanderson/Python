nome = str(input('Qual é o seu nome? '))
if nome == 'Willy':
    print('Que belo nome você tem!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil!')
elif nome in 'Jéssica Cláudia Juliana Ana':
    print('Belo nome feminino!')
else: #Opcional
    print('Seu nome é bem normal!')
print('Tenha um bom dia, {}!'.format(nome))