tupla = ('Chocolate', 'Buceta', 'Peito', 'Fuder', 'Sexo', 'Chupar')

print()

for i in range(0, len(tupla)):
    print(f'A palavra {tupla[i]} possui as vogais: ', end='')
    for j in range(0, len(tupla[i])):
        if (tupla[i][j] == 'a') or (tupla[i][j] == 'e') or (tupla[i][j] == 'i') or (tupla[i][j] == 'o') \
                or (tupla[i][j] == 'u'):
            print(f'{tupla[i][j]} ', end='')
    print()
