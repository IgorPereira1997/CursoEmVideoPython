print('\nNúmeros pares de 1 a 50: ', end=' ')
for i in range(1, 51):
    if i % 2 == 0:
        print('{} '.format(i), end='')
print()