n = 0
somaN = 0
keep = 'S'
allN = []
print()
while keep != 'N':
    n = int(input('Entre com um número (digite 999 para parar o programa): '))
    if n == 999:
        allN.sort()
        break
    somaN += n
    allN.append(n)

print(f'\nQuantidade de números digitados: {len(allN)}\nSoma de todos os números digitados: {somaN}')
