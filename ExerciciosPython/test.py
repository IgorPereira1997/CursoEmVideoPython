import time

print('=== Executando ===')

for i in range(1, 11):
    print(end='\r')
    print('- Processo: {}'.format(i), end='')
    time.sleep(1)  # só para dar tempo de ver a mudança no console

print('\n=== Encerrado ===')