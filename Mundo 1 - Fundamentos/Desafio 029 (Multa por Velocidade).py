velocidade = float(input('Digite a velocidade do carro: '))
m = (velocidade - 80.0) * 7
if velocidade > 80.0:
    print('Você foi multado por ultrapassar o limite de 80km/h!\nO valor da multa é de R${} reais'.format (m))