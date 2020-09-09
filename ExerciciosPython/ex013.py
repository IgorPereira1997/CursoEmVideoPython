n = float(input('Entre com o salário do funcionário: '))
bon = float(input('Entre com a porcentagem de aumento do salário: '))

print('Salário aumentado: R${:.2f}'.format(n*(1+(bon/100))))
