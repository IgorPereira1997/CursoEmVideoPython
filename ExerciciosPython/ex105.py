def notas(num):
    dic = dict()
    dic['quantidade'] = len(num)
    for i in range(0, len(num)):
        if i == 0:
            dic['maior_nota'] = dic['menor_nota'] = num[0]
            dic['media'] = num[i]
        else:
            if num[i] > dic['maior_nota']:
                dic['maior_nota'] = num[i]
            elif num[i] < dic['menor_nota']:
                dic['menor_nota'] = num[i]
            dic['media'] += num[i]
        dic[f'nota_{i}'] = num[i]
    dic['media'] = dic['media'] / dic['quantidade']
    if opcao('a situação do aluno'):
        situation(dic)
        print('\nAdicionado com sucesso.\n')
    return dic


def situation(d):
    if d['media'] < 5:
        d['situacao'] = 'REPROVADO'
    elif d['media'] < 7:
        d['situacao'] = 'RECUPERAÇÃO'
    else:
        d['situacao'] = 'APROVADO'


def notas_turma(n):
    dic = dict()
    for i in range(0, len(n)):
        if i == 0:
            dic['maior_nota_turma'] = n[i]['maior_nota']
            dic['menor_nota_turma'] = n[i]['menor_nota']
        else:
            if n[i]['maior_nota'] > dic['maior_nota_turma']:
                dic['maior_nota_turma'] = n[i]['maior_nota']
            if n[i]['menor_nota'] < dic['menor_nota_turma']:
                dic['menor_nota_turma'] = n[i]['menor_nota']
        dic['media'] = n[i]['media']
    dic['media'] = dic['media'] / len(n)
    if opcao('a situação da turma'):
        situation(dic)
        print('\nAdicionado com sucesso.\n')
    return dic


def entrar_nota(i):
    while True:
        n = input(f'Digite a nota do aluno {i}: ')
        if (not (n.replace('.', '').isdigit())) or float(n) < 0 or float(n) > 10:
            print('\n\033[1;31mERRO! Entrada inválida! Tente novamente!\033[m\n')
        else:
            return float(n)


def opcao(s):
    while True:
        op = input(f'Deseja entrar com {s} [S/N] ? >>> ').upper()
        if op != 'S' and op != 'N':
            print('\n\033[1;31mERRO! Entrada inválida! Tente novamente!\033[m\n')
        else:
            if op == 'S':
                return True
            else:
                return False


def tabela(n):
    print()
    print('=' * 45)
    print('=' * 13 + 'Catálogo de Alunos' + '=' * 13)
    print('=' * 45)
    print(f'|{"Aluno":^21}|{"Notas":^21}|')
    print('=' * 45)

    for i in range(0, len(n) - 1):
        for j in range(0, n[i][f"quantidade"]):
            if j == 0:
                print(f'|{(i + 1):^21}|{round(n[i][f"nota_{j}"], 2):^21}|')
            else:
                print(f'|{"-":^21}|{round(n[i][f"nota_{j}"], 2):^21}|')
        print(f'|{"Maior nota":<21}|{round(n[i]["maior_nota"], 2):^21}|')
        print(f'|{"Menor nota":<21}|{round(n[i]["menor_nota"], 2):^21}|')
        print(f'|{"Média do aluno":<21}|{round(n[i]["media"], 2):^21}|')
        if "situacao" in n[i]:
            print(f'|{"Situação":<21}|{n[i]["situacao"]:^21}|')
        print('=' * 45)
    print('=' * 45)
    print(f'|{"Maior nota da turma":<21}|{round(n[(len(n)-1)]["maior_nota_turma"], 2):^21}|')
    print(f'|{"Menor nota da turma":<21}|{round(n[(len(n)-1)]["menor_nota_turma"], 2):^21}|')
    print(f'|{"Média da turma":<21}|{round(n[(len(n)-1)]["media"], 2):^21}|')
    if "situacao" in n[len(n) - 1]:
        print(f'|{"Situação da turma":<21}|{n[len(n) - 1]["situacao"]:^21}|')
    print('=' * 45)


def main():
    nota = []
    sala = []
    i = 0
    while True:
        print()
        while True:
            nota.append(entrar_nota(i+1))
            if not opcao(f'outra nota do aluno {i+1}'):
                sala.append(notas(nota).copy())
                nota.clear()
                break
        i += 1
        if not opcao('outro aluno'):
            sala.append(notas_turma(sala))
            break
    tabela(sala)


if __name__ == '__main__':
    main()
