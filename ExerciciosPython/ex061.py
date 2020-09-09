numIni = int(input('\nDigite o primeiro termo da progressão aritmética: '))
razao = int(input('Digite a razão da progressão aritmética: '))
termo = numIni
parada = 10
i = 0
while i < parada:
    if i == 0:
        print('\nPrimeiros {} termos da PA: {} ->'.format(parada, termo), end=' ')
    elif i < parada - 1:
        print('{} ->'.format(termo), end=' ')
    else:
        print('{}'.format(termo))
    termo += razao
    i += 1
