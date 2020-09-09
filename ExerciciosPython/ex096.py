def area(a, b):
    return a*b


def valida_dados(s):
    while True:
        data = int(input(f'Entre com {s}: '))
        if data <= 0:
            print('\n\033[1;31mERRO! Entrada inválida! Tente novamente!\033[m\n')
        else:
            return data


def main():
    print()
    largura = valida_dados('a largura')
    comprimento = valida_dados('o comprimento')
    print(f'\nA área do terreno é {area(largura, comprimento):.2f}')


if __name__ == '__main__':
    main()
