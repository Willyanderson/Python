def notas(*n, sit=False):
    """
    -> Função para analizar notas de vários alunos
    :param n: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionario com várias informações sobre a situação da turma.
    """
    b = dict()
    b['Total'] = len(n)
    b['Maior'] = max(n)
    b['Menor'] = min(n)
    b['Média'] = sum(n) / len(n)
    if sit:
        if b['Média'] >= 7:
            b['Situação'] = 'BOA'
        elif b['Média'] >= 5:
            b['Situação'] = 'RAZOÁVEL'
        else:
            b['Situação'] = 'RUIM'
    return b


resp = notas(5.5, 9.5, 10, 6.5, sit=True)
print(resp)
help(notas)