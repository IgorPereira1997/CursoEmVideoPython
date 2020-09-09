n = 0
somaN = 0
keep = 'S'
allN = []

while keep != 'N':
    n = int(input('\nEntre com um número: '))
    somaN += n
    allN.append(n)
    while True:
        keep = str(input('Deseja continuar [S/N]? >>> ')).upper()
        if keep != 'N' and keep != 'S':
            print('\033[1;31mERRO! Entrada inválida! Tente novamente!\033[m')
        elif keep == 'N':
            allN.sort()
            break
        else:
            break
print('\nQuantidade de números digitados: {}\nMédia de todos os números digitados: {}'
      '\nMaior número: {}\nMenor número: {}'.format(len(allN), somaN / len(allN), allN[len(allN) - 1], allN[0]))
