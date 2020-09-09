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
            print(f'\nO dobro de R${value:.2f} é R${moedas.dobro(value, False):.2f}')
            print(f'A metade de R${value:.2f} é R${moedas.metade(value, False):.2f}')
            print(f'Aumentando 15% de R${value:.2f}, tem-se R${moedas.aumentar(value, 15, False):.2f}')
            print(f'Diminuindo 20% de R${value:.2f}, tem-se R${moedas.diminuir(value, 20, False):.2f}')
            flag = True


if __name__ == '__main__':
    main()
