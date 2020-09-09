n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

if n1 == n2:
    print('Números são iguais!')
elif n1 > n2:
    print('Maior número >>> \033[1;31m{}\033[m\nMenor número >>> \033[1;36m{}\033[m'.format(n1, n2))
else:
    print('Maior número >>> \033[1;31m{}\033[m\nMenor número >>> \033[1;36m{}\033[m'.format(n2, n1))
