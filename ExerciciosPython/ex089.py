boletim = []
aluno = []
flag = True


def entrarnome():
    return str(input('\nEntre com o nome do aluno >>> '))


def entrarnota(i):
    while True:
        n = float(input(f'Entre com a nota {i+1}: '))
        if n < 0 or n > 10:
            print('\033[1;31mERRO! Entrada inválida! Tente novamente!\033[m')
        else:
            return n


while flag:
    aluno.append(entrarnome())
    aluno.append(entrarnota(0))
    aluno.append(entrarnota(1))
    aluno.append((aluno[1]+aluno[2])/2)
    while True:
        op = input(f'\nDeseja cadastrar outro Aluno [S/N]? >>> ').upper()
        if op != 'S' and op != 'N':
            print('\033[1;31mERRO! Entrada inválida! Tente novamente!\033[m')
        else:
            if op == 'N':
                flag = False
            break
    boletim.append(aluno[:])
    aluno.clear()

print(f'\n            Aluno(a)            |      Média      ')
for i in range(0, len(boletim)):
    print('{:^32}|{:^17}'.format(boletim[i][0], round(boletim[i][3], 2)))

while not flag:
    op = ''
    while True:
        op = input('\nDeseja ver as notas de algum aluno [S/N] ? >>> ').upper()
        if op != 'S' and op != 'N':
            print('\n\033[1;31mERRO! Entrada inválida! Tente novamente!\033[m')
        else:
            break
    if op == 'S':
        nome = entrarnome()
        if nome in boletim[0]:
            i = boletim[0].index(nome)
            print(f'\nNota 1 : {boletim[i][1]:.2f}; Nota 2: {boletim[i][2]:.2f}')
        else:
            print('\n\033[1;31mERRO! Nome não encontrado!\033[m')
    else:
        flag = True

print('\n\nFINALIZANDO O PROGRAMA.....')
