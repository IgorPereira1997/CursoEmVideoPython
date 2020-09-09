from random import randint


def sorteia(n):
    for i in range(0, 5):
        n.append(randint(0, 100))
    print(f'\nNúmeros sorteados: {n}')


def soma_par(n):
    s = 0
    for i in range(0, len(n) - 1):
        if n[i] % 2 == 0:
            s = s + n[i]
    return s


def main():
    numeros = []
    sorteia(numeros)
    print(f'A soma dos números pares sorteados é {soma_par(numeros)}')


if __name__ == '__main__':
    main()
