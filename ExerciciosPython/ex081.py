valores = list()
i = 0
naList5 = False

print()
while True:
    aux = (int(input(f'Digite o valor {i+1} (Digite 0 para terminar): ')))
    if aux == 0:
        break
    else:
        if aux == 5:
            naList5 = True
        valores.append(aux)
        i += 1

valores.sort(reverse=True)

print(f'\nForam digitados {i} valores\nA lista digitada em ordem decrescente >>> ', end='')

for i in range(0, len(valores)):
    print(f'{valores[i]}  ', end='')

print(f'\nO valor 5 '+ ('foi digitado!' if naList5 else 'não foi digitado!'))


