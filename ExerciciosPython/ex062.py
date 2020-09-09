numIni = int(input('\nDigite o primeiro termo da progressão aritmética: '))
razao = int(input('Digite a razão da progressão aritmética: '))
termo = numIni
parada = 10
i = 0
keep = -1


while i < parada:
    if i < parada - 1:
        if i == 0:
            print('\nPrimeiros {} termos da PA: {} ->'.format(parada, termo), end=' ')
        else:
            print('{} ->'.format(termo), end=' ')
        termo += razao
        i += 1
    else:
        print('{}.'.format(termo), end=' ')
        termo += razao
        i += 1
        break

while keep != 0:
    keep = int(input('Quer mostrar mais termos (0 para encerrar)?: '))
    if keep < 0:
        print('\033[1;31mERRO! Entrada inválida! Tente novamente!\033[m')
    else:
        if keep > 0:
            i = parada
            parada += keep
            while i < parada:
                if keep == 1:
                    print('\nPróximo termo da PA: {}.'.format(termo), end=' ')
                    termo += razao
                    i += 1
                    break
                elif i == (parada - keep):
                    print('\nPróximos {} termos da PA: {} ->'.format(keep, termo), end=' ')
                    termo += razao
                    i += 1
                elif i < parada - 1:
                    print('{} ->'.format(termo), end=' ')
                    termo += razao
                    i += 1
                else:
                    print('{}.'.format(termo), end=' ')
                    termo += razao
                    i += 1
                    break




