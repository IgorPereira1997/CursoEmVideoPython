
preco = 0
op = 0
prest = 0

while True:
    while True:
        preco = float(input('Digite o valor do produto: R$'))
        if preco < 0:
            print('\033[1;31mERRO! Valor inválido!\033[m')
        else:
            break
    while True:
        print("""Método de pagamento\n
        1 - À vista no dinheiro/cheque
        2 - À vista no cartão
        3 - À prazo no cartão
        0 - Cancelar compra\n""")
        op = int(input('Opção: '))
        if op < 0 or op > 3:
            print('\n\033[1;31mERRO, OPÇÃO INVÁLIDA!!!\033[m\n')
        else:
            break
    if op == 0:
        print('\nCOMPRA CANCELADA!!!\n')
        break
    else:
        print()
        if op == 1:
            print('Preço final >>> R${:.2f}'.format(preco*0.9))
        elif op == 2:
            print('Preço final >>> R${:.2f}'.format(preco*0.95))
        else:
            while True:
                prest = float(input('Digite a quantidade de prestações: '))
                if prest < 2:
                    print('\033[1;31mERRO! Quantidade inválida!\033[m')
                else:
                    break
            if prest == 2:
                print('Preço final >>> R${:.2f}'.format(preco))
            else:
                print('Preço final >>> R${:.2f}'.format(preco*1.2))
        print()
