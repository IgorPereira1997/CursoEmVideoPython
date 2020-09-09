dic = {}
people = []
medIdade, qtdMulheres = 0, 0


def entrar_sexo():
    while True:
        s = str(input('Digite o sexo da pessoa [M/F]: ')).upper()
        if s != 'M' and s != 'F':
            print('\n\033[1;31mERRO! Entrada inválida! Tente novamente!\033[m\n')
        else:
            return s


def entrar_idade(s):
    while True:
        idade = int(input(f'Entre com a idade de {s}: '))
        if idade < 0 or idade > 130:
            print('\n\033[1;31mERRO! Entrada inválida! Tente novamente!\033[m\n')
        else:
            return idade


def cadastrar_mais_um():
    op = str(input('\nDeseja cadastrar mais uma pessoa [S/N] ? >>> ')).upper()
    if op != 'S' and op != 'N':
        print('\n\033[1;31mERRO! Entrada inválida! Tente novamente!\033[m\n')
    else:
        return op


while True:
    dic['nome'] = str(input('\nEntre com o nome: '))
    dic['idade'] = entrar_idade(dic['nome'])
    medIdade += dic['idade']
    dic['sexo'] = entrar_sexo()
    people.append(dic.copy())
    op = cadastrar_mais_um()
    if op == 'N':
        break

medIdade = (medIdade/len(people))

print(f'\nQuantidade de pessoas cadastradas >>> {len(people)}\n\nMédia de idade >>> {round(medIdade, 2)}\n')

print('=' * 64)
print('='*24+'Lista de Mulheres'+'='*23)
print('=' * 64)
print(f'|{"Nome":^44}|{"Idade":^17}|')
print('=' * 64)

for i in range(0, len(people)):
    if people[i]['sexo'] == 'F':
        print(f'|{people[i]["nome"]:^44}|{people[i]["idade"]:^17}|')

print('=' * 64)

print(end='\n\n\n')

print('=' * 77)
print('='*18+'Lista de pessoas com idade acima da média'+'='*18)
print('=' * 77)
print(f'|{"Nome":^44}|{"Idade":^17}|{"Sexo":^12}|')
print('=' * 77)

for i in range(0, len(people)):
    if people[i]['idade'] > medIdade:
        print(f'|{people[i]["nome"]:^44}|{people[i]["idade"]:^17}|{people[i]["sexo"]:^12}|')

print('=' * 77)
