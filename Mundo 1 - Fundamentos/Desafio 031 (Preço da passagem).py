p = float(input('Qual vai ser a distância da sua viajem: '))
p1 = p * 0.50
p2 = p * 0.45
if p <= 200:
    print('A viagem custará R${:.2f} reais!'.format(p1)) #R$0,50 por km até 200km
else:
    print('A viagem custará R${:.2f} reais!'.format(p2)) #R$0,45 por km para viajem mais longas que 200km