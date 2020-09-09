valores = list()
print()
for i in range(0, 5):
    valores.append(int(input(f'Entre com o valor {i+1} da lista >>> ')))

valores.sort()

print(f'\nMaior valor: {valores[len(valores)-1]}\nMenor valor: {valores[0]}')
