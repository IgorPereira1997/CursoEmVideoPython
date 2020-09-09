from math import hypot

co = float(input('Digite o comprimento do cateto oposto do triângulo: '))
ca = float(input('Entre com o comprimento do cateto adjacente o triângulo: '))

print('O valor da hipotenusa é {:.4f}'.format(hypot(co, ca)))
