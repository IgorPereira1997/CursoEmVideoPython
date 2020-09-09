dado = list()
people = list()

while True:
    print()
    dado.append(str(input('Entre com o nome da pessoa >>> ')))
    while True:
        aux = float(input(f'Entre com o peso do(a) {dado[0]} >>> '))
        if aux <= 0:
            print('\033[1;31mERRO! Entrada inválida! Tente novamente!\033[m')
        else:
            dado.append(aux)
            break
    while True:
        op = str(input(f'Deseja inserir mais um registro [S/N]? >>> ')).upper()
        if op != 'S' and op != 'N':
            print('\033[1;31mERRO! Entrada inválida! Tente novamente!\033[m')
        else:
            break
    people.append(dado[::-1])
    dado.clear()
    if op == 'N':
        break

people.sort()

print(f'\nNúmero de pessoas cadastradas >>> {len(people)}')
print(f'Pessoas mais pesadas >>> {people[len(people)-1][1]}, com {people[len(people)-1][0]}kg e '
      f'{people[len(people)-2][1]}, com {people[len(people)-2][0]}kg')
print(f'Pessoas mais leves >>> {people[0][1]}, com {people[0][0]}kg e '
      f'{people[1][1]}, com {people[1][0]}kg')
