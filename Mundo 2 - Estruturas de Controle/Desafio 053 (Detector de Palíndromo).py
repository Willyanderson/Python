frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split() #elimina os espaços internos
junto = ''.join(palavras) #juntar(join.()) as palavras sem espaço ('')
inverso = junto[::-1]
print('O inverso de {} é {}.'.format(junto, inverso))
if inverso == junto:
    print('Temos um PALÍNDROMO!')
else:
    print('A frase digitada NÃO É UM PALÍNDROMO!')