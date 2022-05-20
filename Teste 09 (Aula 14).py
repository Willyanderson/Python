'''for c in range(1, 10):
    print(c, end=' ')'''
#O de cima usando for e o de baixo usando while da no mesmo
'''c = 1
while c < 10:
    print(c, end=' ')
    c += 1'''
#A diferença é que o while serve tanto pra quando vc sabe 
#o limite quanto pra quando não sabe, ja o for precisa de um
#limite em sua range() pra atuar.
#EXEMPLOS:

#r = 'S'
#while r == 'S': #enquanto a resposta (r) for sim ('S') irá aparecer n e r
#    n = int(input('Digite um valor: '))
#    r = str(input('Quer continuar?(S/N) ')).upper()
#print('FIM!')

n = 1 #começo da contagem
par = 0 #contagem de números pares começando do 0
impar = 0 #contagem de números ímpares começando do 0
while n != 0: #enquanto o número (n) for diferente (!=) de 0, teremos:
    n = int(input('Digite um valor: '))
    if n != 0: #se o número digitado (n) for diferente de 0, temos:
        if n % 2 == 0: #se o número digitado (n) tiver o resto da divisão (%) por 2 igual a 0:
            par += 1 #ele é par e os números de pares conta +1
        else: #senão:
            impar += 1 #ele é impar e o números de ímpares conta +1
print('Você digitou {} números pares e {} números ímpares.'.format(par, impar))