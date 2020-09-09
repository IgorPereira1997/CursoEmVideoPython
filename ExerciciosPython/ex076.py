tupla = ('Mouse', 67, 'Notebook', 2300, 'Celular', 900, 'Joystick', 100,
         'Capa de Celular', 30)

print()
print(f'        Nome              Preço(R$)      ')

for i in range(0, len(tupla), 2):
    print(f'{tupla[i]:^20}{tupla[i+1]:^21}')
