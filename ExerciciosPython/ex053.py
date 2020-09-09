frase = str(input('\nDigite a frase para verificação se ela é um palíndromo: '))
aux = frase.replace(' ', '').lower()
flag = True
tam = len(aux)
if len(aux) % 2 == 0:
    for i in range(0, int(tam/2) + 1):
        if aux[i] != aux[tam-i-1]:
            flag = False
else:
    for i in range(0, int(tam/2)):
        if aux[i] != aux[tam-i-1]:
            flag = False

print('A frase digitada '+('é um palíndromo!' if flag else 'não é um palíndromo!'))
