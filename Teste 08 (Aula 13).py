#for c in range(0, 6):
#    print('Oi')
#print('FIM')

#for c in range(0, 6):
#    print(c) #se quiser uma contagem de certo número até certo número
#print('FIM')

#for c in range(6, 0, -1): #se quiser uma contagem para trás(regressiva) coloca -1
#    print(c)
#print('FIM')

#for c in range(0, 7, 2): #se quiser uma contagem pulando de tal em tal põe uma virgulo e o numero de pulo
#    print(c)
#print('FIM')

#n = int(input('Digite um número: ')) #Contagem de 0 ate o numero escolhido
#for c in range(0, n+1):
#    print(c)
#print('FIM')

#i = int(input('Início: '))
#f = int(input('Fim: '))
#p = int(input('Passo: ')) #pula do tanto digitado
#for c in range(i, f+1, p):
#    print(c)
#print('FIM!')

#for c in range(0, 4):
#   n = int(input('Digite um número: ')) #irá repetir o comando 4 vezes
#print('Fim!')

#Exemplo do que pode ser feito:

s = 0 
for c in range(0, 4):
    n = int(input('Digite um número: '))
    s += n
print('O somatório de todos os valores foi {}'.format(s))