#Empacotar Parâmetros:
#==> Com Tuplas

'''def contador(*num):
    total = len(num)
    print(f'Recebi os valores {num} e são ao todo {total} valores.')

contador(8, 4, 7)
contador(1, 2, 3, 4, 5)'''


def soma(*valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}.')

soma(5, 2)
soma(2, 9, 4)

#==> Com Listas:

'''def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1

valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)'''