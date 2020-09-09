extenso = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove',
           'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis',
           'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')

n = 0

while True:
    n = int(input('Entre com um número (0 à 20) para ver sua nomenclatura por extenso: '))
    if n < 0 or n > 20:
        print('\033[1;31mERRO! Entrada inválida! Tente novamente!\033[m')
    else:
        break

print(f'{n} por extenso >>> {extenso[n]}')
