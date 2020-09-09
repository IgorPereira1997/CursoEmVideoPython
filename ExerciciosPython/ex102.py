def fatorial(num, show=False):
    f = 1
    if num == 0 or num == 1:
        print(f'{num}! = 1')
    else:
        print()
        for i in range(num, 0, -1):
            f *= num
            if show:
                if i > 1:
                    print(f'{i} X ', end='')
                else:
                    print(f'{i} = {f}')
        if not show:
            print(f'{num}! = {f}')


def entrar_num():
    while True:
        num = input('\nDigite o número para verificação de seu fatorial: ')
        if not (num.isdigit()) or int(num) < 0:
            print('\n\033[1;31mERRO! Entrada de número inválida! Tente novamente!\033[m\n')
        else:
            while True:
                op = input('Deseja mostrar o processo de cálculo [S/N] ? >>> ').upper()
                if op != 'S' and op != 'N':
                    print('\n\033[1;31mERRO! Entrada de resposta inválida! Tente novamente!\033[m\n')
                elif op == 'S':
                    fatorial(int(num), True)
                    break
                else:
                    fatorial(int(num))
                    break
            break


def main():
    entrar_num()


if __name__ == '__main__':
    main()
