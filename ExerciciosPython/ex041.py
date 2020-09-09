from datetime import datetime

while True:
    ano = int(input('\nEntre com o ano de nascimento do atleta: '))
    if (ano < 0) or (ano > datetime.now().year):
        print('\033[1;31mERRO! Idade inválida!\033[m')
    else:
        if (datetime.now().year - ano) <= 9:
            print('\033[1;32mÉ da categoria Mirim\033[m')
        elif (datetime.now().year - ano) <= 14:
            print('\033[1;33mÉ da categoria Infantil\033[m')
        elif (datetime.now().year - ano) <= 19:
            print('\033[1;34mÉ da categoria Junior\033[m')
        elif (datetime.now().year - ano) <= 20:
            print('\033[1;35mÉ da categoria Sênior\033[m')
        else:
            print('\033[1;36mÉ da categoria Máster\033[m')
        break
