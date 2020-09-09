n = float(input('Entre com o preço do produto: '))
d = float(input('Entre com a porcentagem de desconto: '))

print('Preço com o desconto: R${:,.2f}'.format(n*(1-(d/100))))
