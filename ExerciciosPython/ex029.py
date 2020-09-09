while True:
    vel = float(input('\nDigite a velocidade do carro, em km/h: '))
    if vel < 0:
        print('\nErro! Velocidade inválida! Tente novamente!')
    else:
        break
print('\nFOI MULTADO' if vel > 80 else 'NÃO FOI MULTADO', end='')
print('! Multa a ser paga: R${:.2f}'.format((vel-80)*7) if vel > 80 else '')
