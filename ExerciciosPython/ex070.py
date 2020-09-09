produtos = [[] for _ in range(2)]
totPreco = 0
cheap = 0
acima1000 = 0
flag = True
i = 0

while flag:
    produtos[0].append(str(input('\nQual o nome do produto? >>> ')))
    while True:
        aux = float(input('Qual o preço do produto? >>> R$'))
        if aux < 0:
            print('\n\033[1;31mERRO! Entrada inválida! Tente novamente!\033[m')
        else:
            produtos[1].append(aux)
            if i == 0:
                cheap = i
            elif aux < cheap:
                cheap = i
            if aux > 1000:
                acima1000 += 1
            break
    totPreco = totPreco + produtos[1][i]
    while True:
        op = input('\nDeseja continuar [S/N]? >>> ').upper()
        if op != 'S' and op != 'N':
            print('\n\033[1;31mERRO! Entrada inválida! Tente novamente!\033[m')
        elif op == 'N':
            flag = False
            break
        else:
            i += 1
            break
print(f'\nTotal gasto na compra >>> R${totPreco:.2f}\nQuantidade de produtos acima de R$1000.00 >>> {acima1000}'
      f'\nNome do produto mais barato >>> {produtos[0][cheap]}')
