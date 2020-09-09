n = float(input('Digite quantos R$ tem na carteira: '))

print('Cotação do dolar: US$1.00 = R${:,.2f}\nLogo pode com R${:,.2f} você pode comprar US${:,.2f}'
      .format(3.27, n, (n/3.27), 2))
