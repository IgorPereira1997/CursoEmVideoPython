def maior(n):
    if len(n) != 0:
        n.sort()
        return n[len(n) - 1]
    else:
        return 'Não foi digitado nenhum número'


def main():
    num = []
    while True:
        aux = input(f'Digite um número (digite algo não numerico para parar): ')
        if aux.isdigit():
            num.append(aux)
        else:
            print('\nOk, verificando resultados....')
            break
    print(f'\nO maior número digitado foi: {maior(num)}')


if __name__ == '__main__':
    main()
