allN = [[], []]
print()
for i in range(0, 7):
    aux = (int(input('Entre com um número: ')))
    if aux > 0:
        if aux % 2 == 0:
            allN[0].append(aux)
        else:
            allN[1].append(aux)

allN[0].sort()
allN[1].sort()

print(f'\nValores pares digitados em ordem crescente: {allN[0]}.')
print(f'Valores ímpares digitados em ordem crescente: {allN[1]}.')

