alunos = {}
i = 0
sala = []


def entrarnome():
    return str(input('\nEntre com o nome do aluno >>> '))


def entrarnota():
    while True:
        n = float(input(f'Entre com a média do aluno: '))
        if n < 0 or n > 10:
            print('\n\033[1;31mERRO! Entrada inválida! Tente novamente!\033[m\n')
        else:
            return n


while True:
    alunos['nome'] = entrarnome()
    alunos['média'] = entrarnota()
    if alunos['média'] >= 7:
        alunos['situação'] = 'Aprovado'
    elif alunos['média'] >= 5:
        alunos['situação'] = 'Recuperação'
    else:
        alunos['situação'] = 'Reprovado'
    sala.append(alunos.copy())
    while True:
        op = str(input('Deseja inserir outro aluno [S/N] ? >>> ')).upper()
        if op != 'S' and op != 'N':
            print('\n\033[1;31mERRO! Entrada inválida! Tente novamente!\033[m\n')
        else:
            break
    if op == 'N':
        break

print('\n                          Tabela dos alunos           ')
print('---------------------------------------------------------------------')
print('              Nome              |      Média      |     Situação     ')
print('---------------------------------------------------------------------\n')
for i in range(0, len(sala)):
    print('{:^32}|{:^17}|{:^18}'.format(sala[i]['nome'], round(sala[i]['média'], 2), sala[i]['situação']))
print('\n---------------------------------------------------------------------')
