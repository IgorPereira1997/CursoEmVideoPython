import moedas


def validar():
    try:
        p = float(input('Digite o preço desejado: R$'))
        return p
    except:
        print('Erro, valor digitado é inválido!\n\n')
        return False


def main():
    flag = False
    while not flag:
        value = validar()
        if not value:
            pass
        else:
            moedas.resumo(value, 80, 15)
            flag = True


if __name__ == '__main__':
    main()
