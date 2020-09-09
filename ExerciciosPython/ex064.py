n = 0
somaN = 0
qtdN = 0
print()
while n != 999:
    n = int(input('Entre com um número (digite 999 para parar o programa): '))
    if n == 999:
        break
    else:
        somaN += n
        qtdN += 1
print('\nQuantidade de números digitados: {}\nSoma de todos os números digitados: {}'.format(qtdN, somaN))
