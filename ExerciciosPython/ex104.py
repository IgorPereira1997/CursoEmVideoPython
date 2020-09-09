def leia_int(s):
    while True:
        n = input(f'{s}: ')
        if not n.isdigit():
            print('\n\033[1;31mERRO! Não é um número! Tente novamente!\033[m\n')
        else:
            print(f'Voce digitou o número {n}.')
            break


def main():
    leia_int('Digite un número')


if __name__ == '__main__':
    main()
