alt = float(input('Entre com a altura: '))
lar = float(input('Entre com a largura: '))

print('Área da parede {:,.2f}m²'.format(alt*lar))
print('1L de tinta pinta >>> 2m²', end='\nLogo, ')
print('serão necessários {:.2f}L de tinta para pintar a parede'.format((alt*lar)/2))
