n = []
for i in range(1, 4):
    n.append(int(input('Digite o número {}: '.format(len(n)+1))))
n.sort()
print('Maior número digitado: {}\nMenor número digitado: {}'.format(n.pop(len(n)-1), n.pop(0)))
