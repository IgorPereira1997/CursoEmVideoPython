def ficha(nome='<desconhecido>', gols=0):
    print(f'O jogador {nome} fez {gols} gols.')


def entrar_gols(nome):
    while True:
        gols = input('Digite a quantidade de gols: ')
        if not (gols.isdigit()) or int(gols) < 0:
            print('\n\033[1;31mERRO! Entrada inválida! Tente novamente!\033[m\n')
        else:
            if nome == '':
                if int(gols) == 0:
                    ficha()
                else:
                    ficha(gols=int(gols))
            else:
                ficha(nome, int(gols))
            break


def main():
    nome = input('Entre com o nome do jogador: ')
    entrar_gols(nome)


if __name__ == '__main__':
    main()
