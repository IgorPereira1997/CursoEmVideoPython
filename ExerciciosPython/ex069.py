pessoas =[[] for _ in range(3)]
plus18, qtdHomem, woman20minus = 0, 0, 0
aux1, aux2, aux3 = 0, 0, 0
flag = False
while not flag:
    aux1 = str(input('\nNome da pessoa >>>  '))
    while True:
        aux2 = int(input('Qual a idade? >>> '))
        if aux2 < 0:
            print('\033[1;31mERRO! Entrada inválida! Tente novamente!\033[m')
        else:
            break
    while True:
        aux3 = str(input('Qual o sexo [M/F]? >>> ')).upper()
        if aux3 != 'M' and aux3 != 'F':
            print('\033[1;31mERRO! Entrada inválida! Tente novamente!\033[m')
        else:
            break
    pessoas[0].append(aux1)
    pessoas[1].append(aux2)
    pessoas[2].append(aux3)
    if aux2 > 18:
        plus18 += 1
    if aux3 == 'M':
        qtdHomem += 1
    elif aux2 < 20:
        woman20minus += 1
    while True:
        op = str(input('\nDeseja cadastrar outra pessoa [S/N]? >>> ')).upper()
        if op != 'S' and op != 'N':
            print('\033[1;31mERRO! Entrada inválida! Tente novamente!\033[m')
        else:
            break
    if op == 'N':
        flag = True

print(f'\nQuantidade de pessoas com mais de 18 anos >>> {plus18}\nQuantidade de homens >>> {qtdHomem}\n'
      f'Quantidade de mulheres com menos de 20 anos >>> {woman20minus}')
