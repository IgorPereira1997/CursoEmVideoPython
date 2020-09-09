while True:
    ano = int(input('\nDigite o ano para verificar se ele é Bissexto: '))
    if ano < 0:
        print('\nERRO! Ano inválido, tente novamente!')
    else:
        break
print('O ano '+('' if ano % 4 == 0 else 'não ')+'é bissexto!')
