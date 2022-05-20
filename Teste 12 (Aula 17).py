#num = [5, 3, 9, 1]

#num[2] = 3 #Transformação de elementos

#num.append(4) #Adição de elementos (na última posição)

#num.insert(1, 4) #Adição de elementos em qualquer posição

#del num[2]
#num.pop(2) #Excluir elementos
#num.remove(3)

#num = list(range(3, 10, 2)) #Criar listas usando range

#Organização:
#num.sort()  #Ordem crescente
#num.sort(reverse = True)  #Ordem decrescente

#Quantidade de elementos:
#print(len(num))

#print(num)

#EXEMPLO:
valores = []

#valores.append(5)
#valores.append(4)
#valores.append(9)

for cont in range(0, 4):
    valores.append(int(input('Digite um valor: ')))

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}.')