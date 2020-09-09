from random import randint
from operator import itemgetter
results = {}
maior = 0

for i in range(0, 4):
    nome = str(input(f'\nDigite o nome do jogador {i+1}: '))
    results[nome] = randint(1, 6)
    print(f'Resultado do jogador {i+1} registrado!')

ranking = sorted(results.items(), key=itemgetter(1), reverse=True)

for i, v in enumerate(ranking):
    print(f'\n {i+1}º Lugar >>> {v[0]}, com valor {v[1]}')
