matriz = [[], [], []]
somaP = 0
soma3Row = 0
maior2Row = 0
for i in range(0, 3):
    for j in range(0, 3):
        matriz[i].append(int(input(f'Digite um valor para o termo [{i}, {j}]: ')))
        if matriz[i][j] % 2 == 0:
            somaP += matriz[i][j]
        if j == 2:
            soma3Row += matriz[i][j]
        if i == 1:
            if j == 0:
                maior2Row = matriz[i][j]
            elif maior2Row < matriz[i][j]:
                maior2Row = matriz[i][j]

print('\n=======================================')
for i in range(0, 3):
    for j in range(0, 3):
        print(f'[{matriz[i][j]:^9}]', end='')
    print()
print('=======================================')
print(f'\nSoma de todos os valores pares >>> {somaP}\nSoma dos valores da 3ª coluna >>> {soma3Row}\n'
      f'Maior valor da 2ª linha >>> {maior2Row}')
