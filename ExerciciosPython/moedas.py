def aumentar(num, por, formatar):
    if formatar:
        return moeda(num * (1 + (por / 100)))
    else:
        return num * (1 + (por / 100))


def diminuir(num, por, formatar):
    if formatar:
        return moeda(num * (1 - por / 100))
    else:
        return num * (1 - por / 100)


def dobro(num, formatar):
    if formatar:
        return moeda(num*2)
    else:
        return num*2


def metade(num, formatar):
    if formatar:
        return moeda(num/2)
    else:
        return num/2


def moeda(num):
    return f'{num:.2f}'


def resumo(num, plus, down):
    print('\n')
    print('='*52)
    print('=' * 19, 'RESUMO VALOR', '=' * 19)
    print('=' * 52)
    print('{:^30}|{:^22}'.format("Valor informado", ("R$" + moeda(num))).center(22))
    print('{:^30}|{:^22}'.format("Dobro do valor", ("R$" + dobro(num, True)).center(22)))
    print('{:^30}|{:^22}'.format("Metade do valor", ("R$" + metade(num, True)).center(22)))
    print('{:^30}|{:^22}'.format(f"{plus}% de aumento", ("R$" + aumentar(num, plus, True)).center(22)))
    print('{:^30}|{:^22}'.format(f"{down}% de redução", ("R$" + diminuir(num, down, True))).center(22))
    print('=' * 52)



