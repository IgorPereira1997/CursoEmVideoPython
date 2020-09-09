while True:
    op = str(input('Digite o seu sexo: ')).upper()
    if op != 'M' and op != 'F':
        print('\033[1;31mERRO! Entrada inválida! Tente novamente!\033[m')
    else:
        break
