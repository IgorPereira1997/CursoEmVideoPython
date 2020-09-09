from random import randint

sorteios = list()
jogo = list()

n = 0
print()
while True:
    n = int(input('Quantos jogos você quer gerar? >>> '))
    if n <= 0:
        print('\033[1;31mERRO! Entrada inválida! Tente novamente!\033[m')
    else:
        break
print('\n================================================')
for i in range(0, n):
    for j in range(0, 6):
        jogo.append(randint(1, 60))
    sorteios.append(jogo[:])
    jogo.clear()

for i in range(0, n):
    print(f'Jogo {i+1}: {sorteios[i]}')
print('================================================')
