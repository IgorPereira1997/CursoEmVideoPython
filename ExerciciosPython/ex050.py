s = 0
print()
for i in range(1, 7):
    n = int(input('Entre com o numero {}: '.format(i)))
    if i % 2 == 0:
        s += i
print('\nSoma dos números pares digitados: {}'.format(s))
