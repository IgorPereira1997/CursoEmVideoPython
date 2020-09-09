print('\033[31m\nOlá, mundo!')
print('\033[31;43mOlá, mundo!\033[m')
print('\033[1;31;43mOlá, mundo!\033[m')
print('\033[4;30;45mOlá, mundo!\033[m')
print('\033[30mOlá, mundo!\033[m')
print('\033[37mOlá, mundo!\033[m')
print('\033[7;30mOlá, mundo!\033[m')
print('\033[0;33;44mOlá, mundo!\033[m')
print('\033[7;33;44mOlá, mundo!\033[m')

nome = 'Igor'
cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'amarelo': '\033[33m',
         'pretoebranco': '\033[7;30m'}
print('Muito prazer em te conhecer, {}{}{}!!!!'.format(cores['amarelo'], nome, cores['limpa']))
