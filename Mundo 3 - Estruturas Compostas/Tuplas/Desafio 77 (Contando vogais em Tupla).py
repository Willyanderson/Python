palavras = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 
'PYTHON', 'CURSO', 'GRATIS', 'ESTUDAR', 'TRABALHAR', 
'MERCADO', 'PRATICAR', 'FUTURO', 'CURSO')
for p in palavras:
    print(f'\nNa palavra {p} temos ', end = '')
    for letra in p:
        if letra in 'AEIOU':
            print(letra, end = ' ')