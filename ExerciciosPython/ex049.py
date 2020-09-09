n = int(input('Entre com o número: '))

print('Tabuada do {}'.format(n),end=' >>> \n\n')
for i in range(1, 11, 1):
    print('{:2} X {} = {:3}'.format(i, n, (i*n)))
