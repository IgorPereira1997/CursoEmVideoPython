val = []
flag = True
par = 0
for i in range(0, 4):
    val.append(int(input(f'Digite o valor {i+1}: ')))

tupla = ( val[0], val[1], val[2], val[3])

print(f'Vezes que o número 9 apareceu: {tupla.count(9)}')

for i in range(0, len(tupla)):
    if tupla[i] == 3:
        print(f'3 foi digitado na {i+1}ª posição')
        flag = False

if flag:
    print('O número 3 não se encontra na tupla')

for i in range(0, len(tupla)):
    if tupla[i] % 2 == 0:
        par += 1

print(f'Quantidade de números pares digitados: {par}')
