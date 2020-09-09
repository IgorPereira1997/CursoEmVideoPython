from datetime import datetime


while True:
    n = int(input('\nEntre com o ano de nascimento: '))
    if (n < 0) or (n > datetime.now().year):
        print('ERRO! Ano inválido! Tente novamente!')
    else:
        if (datetime.now().year - n) < 18:
            print('\033[1;32mAinda irá se alisatar, dentro de\033[1;35m {} \033[1;32mano(s)!\033[m'
                  .format(18 - (datetime.now().year-n)))
        elif (datetime.now().year - n) == 18:
            print('\033[1;33mHora de se alisatar!\033[m')
        elif (datetime.now().year - n) >= 70:
            print('\033[1;36mNão pode mais se alistar, idade avançada\033[m')
        else:
            print('\033[1;32mPassou do tempo de se alisatar há\033[1;35m {} \033[1;32mano(s)!\033[m'
                  .format((datetime.now().year - n)-18))
        break
