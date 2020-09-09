number = []


def entrada(n):
    n.append(int(input('\nEntre com o primeiro número: ')))
    n.append(int(input('Entre com o segundo número ')))


entrada(number)

while True:
    print("""\nMenu de opções
        [1] Somar
        [2] Multiplicar
        [3] Maior
        [4] Novos números
        [5] Sair""")
    op = int(input('Opção: '))
    if op < 1 or op > 5:
        print('\033[1;31mERRO! Entrada inválida! Tente novamente!\033[m')
    elif op == 1:
        print('\n{} + {} = {}'.format(number[0], number[1], number[0]+number[1]))
    elif op == 2:
        print('\n{} X {} = {}'.format(number[0], number[1], number[0]*number[1]))
    elif op == 3:
        print('\nMaior valor: {}'.format(number[0] if number[0] > number[1] else number[1]))
    elif op == 4:
        number.clear()
        entrada(number)
    else:
        print('\n\033[7;30mOBRIGADO POR UTILIZAR O PROGRAMA!!!!\033[m')
        break
