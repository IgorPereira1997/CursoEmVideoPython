matriz = [[], [], []]

for i in range(0, 3):
    for j in range(0, 3):
        matriz[i].append(int(input(f'Digite um valor para o termo [{i}, {j}]: ')))
print('=======================================')
for i in range(0, 3):
    for j in range(0, 3):
        print(f'[{matriz[i][j]:^9}]', end='')
    print()
