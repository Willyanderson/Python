try:
    a = int(input('Numerador: '))
    b = int(input('Divisor: '))
    r = a / b

#except:
#    print('Infelismente tivemos um problema...')
except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados que você digitou.')
except ZeroDivisionError:
    print('Não é possível dividir um número por 0!')
except KeyboardInterrupt:
    print('O usúario preferiu não informar os dados.')
except Exception as erro: #-->Exibir qual foi o Erro
    print(f'O problema foi {erro.__class__}')

else:
    print(f'O resultado é {r:.1f}')
finally:
    print('Volte Sempre! Muito obrigado!')