n1 = 0
n2 = 0
while True:
    n1 = float(input('\nEntre com a primeira nota: '))
    if n1 < 0 or n1 > 10:
        print('\033[1;31mERRO! Nota Inválida!\033[m')
    else:
        break
while True:
    n2 = float(input('Entre com a segunda nota: '))
    if n2 < 0 or n2 > 10:
        print('\033[1;31mERRO! Nota Inválida!\033[m')
    else:
        break
print()
if (n1 + n2)/2 < 5:
    print('\033[1;31mREPROVADO\033[m')
elif (n1 + n2)/2 <= 6.9:
    print('\033[1;33mRECUPERAÇÃO\033[m')
else:
    print('\033[1;32mAPROVADO\033[m')
