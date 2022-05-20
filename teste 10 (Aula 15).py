#while True: Looping infinito
#break: Comando que quebra o looping infinito
n = soma = 0
while True:
    n = int(input('Digite um número [999 para parar]: '))
    if n == 999:
        break
    soma += n
print(f'A soma de todos os números vale {soma}') #Nova escrita seguindo a "fstring"