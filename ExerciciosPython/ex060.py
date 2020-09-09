while True:
    n = int(input('\nEntre com o número para cálculo de seu fatorial: '))
    if n < 0:
        print('\033[1;31mERRO! Entrada inválida! Tente novamente!\033[m')
    else:
        break
s = 1
if n == 0 or n == 1:
    print('{}! = 1'.format(n))
else:
    aux = n
    while aux > 1:
        s *= aux
        aux -= 1
    print('{}! = {}'.format(n, s))
