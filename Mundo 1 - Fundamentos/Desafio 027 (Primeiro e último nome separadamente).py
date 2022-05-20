nome = str(input('Digite seu nome completo: ')).strip()
separação = nome.split()
print('Seu primeiro nome é: {}'.format(separação[0]))
print('Seu último nome é: {}'.format(separação[len(separação) - 1]))