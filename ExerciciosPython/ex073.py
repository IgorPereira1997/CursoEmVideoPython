brasileiro = ('Athetico', 'Atlético-MG', 'Avaí', 'Bahia', 'Botafogo', 'Ceará',
              'Chapecoense', 'Corinthians', 'Cruzeiro', 'CSA', 'Flamengo',
              'Fluminense', 'Fortaleza', 'Goiás', 'Grêmio', 'Internacional',
              'Palmeiras', 'Santos', 'São Paulo', 'Vasco')

print(f'\nPrimeiros 5 colocados: {brasileiro[:5]}')
print(f'Últimos 4 colocados: {brasileiro[16:20]}')
print(f'Times em ordem alfabética: {sorted(brasileiro)}')

for i in range(0, len(brasileiro)):
    if brasileiro[i] == 'Chapecoense':
        print(f'A Chapecoense está ná {i+1}ª posição')
        break
