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
            print(f'\nO dobro de R${moedas.moeda(value)} é R${moedas.moeda(moedas.dobro(value, False))}')
            print(f'A metade de R${moedas.moeda(value)} é R${moedas.moeda(moedas.metade(value, False))}')
            print(
                f'Aumentando 15% de R${moedas.moeda(value)}, tem-se R${moedas.moeda(moedas.aumentar(value, 15, False))}'
            )
            print(
                f'Diminuindo 20% de R${moedas.moeda(value)}, tem-se R${moedas.moeda(moedas.diminuir(value, 20, False))}'
            )
            flag = True


if __name__ == '__main__':
    main()
