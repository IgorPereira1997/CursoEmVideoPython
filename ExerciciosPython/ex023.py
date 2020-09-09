num = ''
while True:
    num = input('\nDigite um número entre 0 e 9999: ')
    if (int(num) < 0) or (int(num) > 9999):
        print('ERRO, número inválido!\nTENTE NOVAMENTE!!!', end='\n')
    else:
        break
i = len(num)
aux = []
for i in range(i, 4):
    aux.append('0')
for j in range(0, len(num)):
    aux.append(num[j])

print('\nMilhares: {}\nCentenas: {}\nDezenas: {}\nUnidades: {}'.format(aux[0], aux[1], aux[2], aux[3]))

