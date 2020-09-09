from random import randint
import time
while True:
    print("""Jogo jokenpô
            1 - pedra
            2 - papel
            3 - tesoura
            0 - sair""")
    op = int(input('Opção de escolha: '))
    if op < 0 or op > 3:
        print('\n\033[1;31mERRO! Opção inválida!\033[m')
    elif op == 0:
        print('\n\033[7;30mOBRIGADO POR JOGAR!!!!\033[m')
        break
    else:
        comp = randint(1, 3)
        print('JO')
        time.sleep(0.5)
        print('KEN')
        time.sleep(0.5)
        print('PÔ!!!')
        time.sleep(0.5)
        if comp == op:
            print('\n\033[1;33mEMPATE\033[m\n')
        elif (op == 1 and comp == 3) or (op == 2 and comp == 1) or (op == 3 and comp == 2):
            print('\n\033[1;32mGANHOU\033[m\n')
        else:
            print('\n\033[1;31mPERDEU\033[m\n')
