def entrar_idade():
    while True:
        idade = input('Digite a idade da pessoa: ')
        if not (idade.isdigit()) or int(idade) < 0:
            print('\n\033[1;31mERRO! Entrada inválida! Tente novamente!\033[m\n')
        else:
            return voto(int(idade))


def voto(idade):
    if int(idade) < 16:
        return 'NEGADO'
    elif int(idade) < 18 or int(idade) > 70:
        return 'OPICIONAL'
    else:
        return 'OBRIGARORIO'


def main():
    print(f'Situação de voto da pessoa informada: {entrar_idade()}')


if __name__ == '__main__':
    main()
