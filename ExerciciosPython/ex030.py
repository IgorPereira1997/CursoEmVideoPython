while True:
    n = int(input('\nDigite um número natura para saber se é par ou ímpar: '))
    if n < 0:
        print('\nERRO! Valor inválido, tente novamente!')
    else:
        break
print('\n{} é um número '.format(n)+('PAR' if n % 2 == 0 else 'ÍMPAR'))
