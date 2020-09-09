valores = list()

for i in range(0, 5):
    flag = False
    j = 0
    aux = int(input(f'Entre com o valor {i+1}: '))
    if len(valores) == 0:
        valores.append(aux)
        continue
    else:
        for j in range(0, len(valores)):
            if aux < valores[j]:
                flag = True
                valores.insert(j, aux)
                break
        if not flag:
            valores.append(aux)


print(f'Lista digitada ordenada >>> ', end='')
for i in range(0, len(valores)):
    print(f'{valores[i]}  ', end='')

