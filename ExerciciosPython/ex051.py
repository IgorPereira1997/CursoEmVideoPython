numIni = int(input('\nDigite o primeiro termo da progressão aritmética: '))
razao = int(input('Digite a razão da progressão aritmética: '))
termo = numIni
parada = 10
for i in range(1, parada + 1):
    if i == 1:
        print('\nPrimeiros {} termos da PA: {} ->'.format(parada, termo), end=' ')
    elif i < parada:
        print('{} ->'.format(termo), end=' ')
    else:
        print('{}'.format(termo))
    termo += razao
    i += 1
