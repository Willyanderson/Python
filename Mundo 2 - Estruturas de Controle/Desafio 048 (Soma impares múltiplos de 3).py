soma = 0 #acumulador
cont = 0 #contador
for c in range(1 , 500, 2): #numeros impares
    if c % 3 == 0: #se c for divisivel por 3
        soma += c #acumulador
        cont += 1 #contador
print('A soma de todos os {} valores solicitados é {}!'.format(cont, soma))