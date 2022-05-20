def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mERRO: por favor, digite um número inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[0;31mUsúario preferiu não digitar esse número!\033[m')
            return 0
        else:
            return n 


def leiaFloat(msgm):
    while True:
        try:
            v = float(input(msgm))
        except (ValueError, TypeError):
            print('\033[0;31mERRO: por favor, digite um número inteiro válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[0;31mUsúario preferiu não digitar esse número!\033[m')
            break
        else:
            return v
                
   
i = leiaInt('Digite um Inteiro: ')
r = leiaFloat('Digite um Real: ')
print(f'O valor inteiro digitado foi {i} e o real foi {r}')