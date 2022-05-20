peso = float(input('Peso (ex.:69.2): '))
altura = float(input('Altura (ex.:1.70): '))
imc = peso / (altura ** 2)
print()
print('O IMC dessa pessoa é de {:.1f}'.format(imc))
if imc < 18.5:
    print('Status: ABAIXO DO PESO')
elif 18.5 <= imc < 25:
    print('Status: PESO NORMAL')
elif 25 <= imc < 30:
    print('Status: SOBREPESO')
elif 30 <= imc < 40:
    print('Status: OBSIDADE')
else:
    print('Status: OBSIDADE MÓRBIDA')