from time import sleep


def contador(inicio, fim, passo):
    print()
    if inicio > fim:
        for i in range(inicio, fim - 1, -passo):
            print(f'\r{i}', end='')
            sleep(1)
    else:
        for i in range(inicio, fim + 1, passo):
            print(f'\r{i}', end='')
            sleep(1)
    print()


def valida_dados(s):
    while True:
        data = input(f'Digite o valor para {s}: ')
        if not data.isnumeric():
            print('\n\033[1;31mERRO! Entrada inválida! Tente novamente!\033[m\n')
        else:
            return int(data)


def main():
    print()
    contador(valida_dados('o início da contagem'), valida_dados('o fim da contagem'),
             valida_dados('o passo da contagem'))


if __name__ == '__main__':
    main()
