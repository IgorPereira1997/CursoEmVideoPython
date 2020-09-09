qtd50, qtd20, qtd10, val, valOrig = 0, 0, 0, 0, 0

while True:
    valOrig = int(input('\nDigite o valor que deseja sacar >>> R$'))
    if valOrig <= 0:
        print('\033[1;31mERRO! Entrada inválida! Tente novamente!\033[m')
    else:
        break

val = valOrig

qtd50 = int(val / 50)
val = int(val % 50)

qtd20 = int(val / 20)
val = int(val % 20)

qtd10 = int(val / 10)
val = int(val % 10)

print(f'\nSerão entregues as seguintes cédulas para entragar seus R${valOrig} >>>'
      f'\n\nR$50 >>> {qtd50}\nR$20 >>> {qtd20}\nR$10 >>> {qtd10}\nR$1 >>> {val}')
