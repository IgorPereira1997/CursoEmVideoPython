fibo = [0, 1]
i = 0
while True:
    n = int(input('\nDigite quantos termos da série de fibonnaci você deseja (0 para sair): '))
    if n < 0:
        print('\033[1;31mERRO! Entrada inválida! Tente novamente!\033[m')
    else:
        if n == 1:
            print('Primeiro termo da série Fibonacci: {}'.format(fibo[0]), end='')
            break
        while i < n:
            if i == 0:
                print('Primeiros {} termos da série Fibonacci: {}'.format(n, fibo[i]), end='')
            elif i == 1:
                print(' -> {}'.format(fibo[i]), end='')
            else:
                fibo.append(fibo[i-2]+fibo[i-1])
                print(' -> {}'.format(fibo[len(fibo)-1]), end='')
            i += 1
        print('.')
        break
