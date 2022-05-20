a = float(input('Altura da parede (em metros): '))
l = float(input('Largura da parede (em metros): '))
a2 = a * l
ql = a2 / 2
print('A área da parede é de {:.2f} metros² que equivale a {:.0f} latas de tinta!'.format(a2,ql))