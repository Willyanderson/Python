print(13 * '=-=')
print('{:^39}'.format('Constrções Stardew Valley'))
print(13 * '=-=')
valor = barra = coco = cacto = coral = concha = cristal = carambola = fibra = pedra = 0
cons = ('Obelisco de Água', 'Obelisco do Deserto', 'Obelisco da Terra', 'Cabana dos junimos', 'Relógio Dourado')
for p, c in enumerate(cons):   
    print(f'[{p+1}] ➝  {c}')
print()
while True:
    opc = int(input('Qual contrução você quer ter: '))    
    if opc == 1:
        valor += 500000
        barra = 5
        concha = 10
        coral = 10
    elif opc == 2:
        valor += 1000000
        barra += 20
        coco = 10
        cacto = 10
    elif opc == 3:
        valor += 500000
        barra += 10
        cristal = 10
    elif opc == 4:
        q = int(input('Quantidade: '))
        valor += 20000 * q
        pedra = 200 * q
        carambola = 9 * q
        fibra = 100 * q
    elif opc == 5:
        valor += 10000000
    x = str(input('Vai querer mais alguma coisa [S/N]? ')).strip().upper()
    if x in 'N':
        break    
print(13 * '=-=')
if barra > 0:
    print(f'Barras de Íridio: {barra}')
if concha > 0:
    print(f'Conchas: {concha}')
if coral > 0:
    print(f'Coral: {coral}')
if coco > 0:
    print(f'Coco: {coco}')
if cristal > 0:
    print(f'Cristal da Terra: {cristal}')
if pedra > 0:
    print(f'Pedras: {pedra}')
if carambola > 0:
    print(f'Carambolas: {carambola}')
if fibra > 0:
    print(f'Fibras: {fibra}')
print(f'Valor Total: {valor} moedas')
print(13 * '=-=')