from random import randint
inv = ''
vic = 0
print('\n============================================\n JOGO PAR OU ÍMPAR '
      '\n============================================')
while True:
    while True:
        n = int(input('Entre com um número: ')).__abs__()
        op = str(input('Deseja escolher par ou impar? >>> ')).lower()
        if op != 'par' and op != 'impar':
            print('\033[1;31mERRO! Entrada inválida! Tente novamente!\033[m')
        else:
            if op == 'par':
                inv = 'impar'
            else:
                inv = 'par'
            break
    pc = randint(1, 10)
    if (op == 'par' and (n + pc) % 2 == 1) or (op == 'impar' and (n + pc) % 2 == 0):
        print(f'PERDEEEEEEU OTÁRIO!\nEscolhi {pc} e você {n}, gerando {pc+n}, que é {inv}'
              f'\nNúmero de vitórias seguidas: {vic}')
        print('============================================')
        break
    vic += 1
    print(f'GANHOU!\nEscolhi {pc} e você {n}, gerando {pc+n}, que é {op}\nVAMOS CONTINUAR....')
    print('\n============================================')
