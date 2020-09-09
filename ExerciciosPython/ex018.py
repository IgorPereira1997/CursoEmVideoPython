from math import sin, cos, tan, radians

n = float(input('Digite um ângulo para verificação de suas informações: '))

print('Ângulo: {}'.format(n), end=' >>> \n')
print('\nSeno: {}\nCosseno: {}\nTangente: {}'.format(sin(radians(n)), cos(radians(n)), tan(radians(n))))
