from random import randint
flag = True
qtdPalpite = 1
while flag:
    while True:
        palpite = int(input('\nDigite o palpite du número digitado pelo computador (0 à 10): '))
        if palpite < 0 or palpite > 10:
            print('\nOpa! Palpite inválido!\nTente novamente!!!', end='\n')
        else:
            break
    n = randint(0, 10)
    if palpite != n:
        print('\nERROU!!')
        qtdPalpite += 1
    else:
        flag = False
        print('\nACERTOU! Foram necesários {} palpites para acerto'.format(qtdPalpite))
