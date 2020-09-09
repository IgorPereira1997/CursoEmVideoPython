while True:
    sal = float(input('\nDigite o seu salário para cálculo do aumento: '))
    if sal <= 0:
        print('\nERRO! Valor inválido! Tente novamente!')
    else:
        break
print('Valor do salário com aumento >>> R${:.2f} + R$'.format(sal) +
      ('{:.2f}: [R${:.2f}]'.format(sal*0.1, sal*0.1+sal) if sal > 1250
       else '{:.2f}: [R${:.2f}]'.format(sal*0.15, sal*0.15+sal)))
