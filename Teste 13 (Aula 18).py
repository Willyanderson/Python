#teste = []
#teste.append('Gustavo')
#teste.append(40)
#galera = list()
#galera.append(teste[:])
#teste[0] = ('Maria')
#teste[1] = (25)
#galera.append(teste[:])
#print(galera)

galera = [['João', 25], ['Rafa', 15], ['Maria', 19]]
#print(galera[0][0])
#print(galera[1])

#for p in galera:
#    print(p) #Listas

#for n in galera:
#    print(n[0]) #Só os nomes, pois todos estão nos índices 0 das listas

#for i in galera:
#    print(i[1]) #Só as idades, mesmo motivo do anterior

for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade!')