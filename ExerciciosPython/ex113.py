def leia_int():
    while True:
        try:
            n = float(input('Digite um número: '))
        except:
            print('\n\033[1;31mERRO! Não é um número! Tente novamente!\033[m\n')
        else:
            print(f'Voce digitou o número {n:.3f}.')
            break


def main():
    leia_int()


if __name__ == '__main__':
    main()
