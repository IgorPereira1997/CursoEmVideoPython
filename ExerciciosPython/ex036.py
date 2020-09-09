valCasa = float(input('Entre com o valor da casa: R$'))
sal = float(input('Entre com o seu salário: R$'))
anos = int(input('Entre com quantos anos você deseja pagar a casa: '))
print('Empréstimo '+('aprovado!' if ((valCasa)/(anos*12)) <= (sal*0.3) else 'negado!'))
