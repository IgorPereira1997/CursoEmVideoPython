dic = {}
i = 0
players = []

def quantas_partidas():
    while True:
        qp = int(input('Digite o número de partidas que o jogador fez: '))
        if qp < 0 or qp > 38:
            print('\033[1;31mERRO! Entrada inválida! Tente novamente!\033[m')
        else:
            return qp


def quantos_gols(j):
    while True:
        qg = int(input('Digite o número de gols que o jogador fez na partida {}: '.format(j+1)))
        if qg < 0 or qg > 13:
            print('\033[1;31mERRO! Entrada inválida! Tente novamente!\033[m')
        else:
            return qg


def cadastrar_mais_um():
    op = str(input('\nDeseja cadastrar mais uma pessoa [S/N] ? >>> ')).upper()
    if op != 'S' and op != 'N':
        print('\n\033[1;31mERRO! Entrada inválida! Tente novamente!\033[m\n')
    else:
        return op


while True:
    dic['nome'] = str(input('\nEntre com o nome do jogador: '))
    i = quantas_partidas()
    if i > 0:
        dic['total de gols'] = 0
        for j in range(0, i):
            dic[f'partida {j+1}'] = quantos_gols(j)
            dic['total de gols'] += dic[f'partida {j+1}']
        dic['qtd partidas'] = i
        i = 0
    else:
        dic['qtd partidas'] = 0
        dic['nao_jogou'] = 'O jogador não entrou em campo em nenhum partida'
    players.append(dic.copy())
    op = cadastrar_mais_um()
    if op == 'N':
        break

print()
print('=' * 90)
print('=' * 28+'Catálogo de Jogadores do Campeonato'+'='*27)
print('=' * 90)
print(f'|{"Nome":^40}|{"Partida":^22}|{"Gols Marcados":^24}|')
print('=' * 90)

for j in range(0, len(players)):
    if players[j]['qtd partidas'] == 0:
        print(f'|{players[j]["nome"]:^40}|{players[j]["nao_jogou"]:^40}|')
        print('=' * 90)
    else:
        for k in range(0, players[j]['qtd partidas']):
            if k == 0:
                print(f'|{players[j]["nome"]:^40}|{(k+1):^22}|{players[j][f"partida {k+1}"]:^24}|')
            else:
                print(f'|{"":^40}|{(k + 1):^22}|{players[j][f"partida {k + 1}"]:^24}|')
                if k == (players[j]['qtd partidas'] - 1):
                    print('.'*90)
                    print(f'|{"Total de gols":<63}|{players[j]["total de gols"]:^24}|')
                    print('=' * 90)
print('=' * 90)
