valores = list()
impar = list()
par = list()
j = 0
print()
while True:
    aux = int(input(f'Digite o valor {j+1} (digite 0 para encerrar o programa) >>>> '))
    if aux == 0:
        break
    else:
        valores.append(aux)
        if aux > 0:
            if aux % 2 == 0:
                par.append(aux)
            elif aux % 2 != 0:
                impar.append(aux)
        j += 1

print(f'\nA lista com todos os números digitados >>>', end='')
valores.sort()
for i in range(0, len(valores)):
    print(f'  {valores[i]}', end='')
    if i == (len(valores) - 1):
        print('.\n')


print(f'\nA lista com todos os números pares >>>', end='')
par.sort()
for i in range(0, len(par)):
    print(f'  {par[i]}', end='')
    if i == (len(par) - 1):
        print('.\n')


print(f'\nA lista com todos os números ímpares >>>', end='')
impar.sort()
for i in range(0, len(impar)):
    print(f'  {impar[i]}', end='')
    if i == (len(impar) - 1):
        print('.\n')

