dia = int(input('Quantos dias foi alugado? '))
dist = float(input('Quantos km rodados? '))

custo = ((60*dia) + (0.15*dist))

print('O total a pagar é R${:.2f}'.format(custo))
