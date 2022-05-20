num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
if num1 > num2:
    print('{} é maior do que {}!'.format(num1, num2))
elif num1 < num2:
    print('{} é menor do que {}!'.format(num1, num2))
else:
    print('Não existe valor maior, os dois são IGUAIS!')