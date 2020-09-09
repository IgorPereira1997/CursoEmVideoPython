import time


def int2bin(n):
    b = ''
    while n != 0:
        b += str(n % 2)
        n = int(n / 2)
    return b[::-1]


def int2oct(n):
    o = ''
    while n != 0:
        o += str(n % 8)
        n = int(n / 8)
    return o[::-1]


def int2hex(n):
    h = ''
    while n != 0:
        if n % 16 <= 9:
            h += str(n % 16)
        elif n % 16 == 10:
            h += 'A'
        elif n % 16 == 11:
            h += 'B'
        elif n % 16 == 12:
            h += 'C'
        elif n % 16 == 13:
            h += 'D'
        elif n % 16 == 14:
            h += 'E'
        else:
            h += 'F'
        n = int(n / 16)
    return h[::-1]


def main():
    while True:
        while True:
            print("""Base de conversão\n
            1 - binário
            2 - octal
            3 - hexadecimal
            0 - sair\n""")
            op = int(input('Opção: '))
            if op < 0 or op > 3:
                print('\nERRO, OPÇÃO INVÁLIDA!!!\n')
            else:
                break
        if op == 0:
            print('\nOBRIGADO POR UTILIZAR O PROGRAMA!!!\n')
            break
        else:
            num = int(input('\nEntre com um número inteiro: '))
            if op == 1:
                print('{} convertido para binário >>>'.format(num), int2bin(num))
            elif op == 2:
                print('{} convertido para octal >>>'.format(num), int2oct(num))
            else:
                print('{} convertido para hexadecimal >>>'.format(num), int2hex(num))
            time.sleep(5)
    return 0


if __name__ == "__main__":
    main()
