salário = float(input('Digite o valor de seu salário: '))
aumento1 = salário * (11/10)
aumento2 = salário * (115/100)
if salário >= 1250: #Para salários maiores que 1250,00 o aumento será de 10%, para menores que isso será de 15%
    print('Com o salário de R${:.2f} reais você irá receber um aumento de 10%,\nelevendo seu salário para R${:.2f} reais!'.format(salário, aumento1))
else:
    print('Com o salário de R${:.2f} reais você irá receber um aumento de 15%,\nelevando seu salário para R${:.2f} reias!'.format(salário, aumento2))