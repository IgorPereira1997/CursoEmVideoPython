from random import randint

while True:
    palpite = int(input('Digite o palpite du número digitado pelo computador (0 à 5): '))
    if palpite < 0 or palpite > 5:
        print('\nOpa! Palpite inválido!\nTente novamente!!!', end='\n')
    else:
        break
n = randint(0, 5)
print('ACERTOU!' if palpite == n else 'ERROU')
