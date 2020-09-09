valores = list()

for i in range(0, 5):
    aux = (int(input(f'Digite o valor {i+1} da lista >>> ')))
    if not(aux in valores):
        valores.append(aux)

print(f'Valores únicos digitados em ordem crescente >>> ', end='')
valores.sort()
for i in range(0, len(valores)):
    print(f'{valores[i]}  ', end='')

