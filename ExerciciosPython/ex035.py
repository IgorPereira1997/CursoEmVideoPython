ladosT = []
answer = 'não podem formar um triângulo'
print('\nPrograma para verificar a formação ou não de um triângulo\n')
for i in range(1, 4):
    while True:
        aux = float(input('Digite a reta {}: '.format(i)))
        if aux < 0:
            print('\nERRO! Valor inválido, tente novamente!')
        else:
            ladosT.append(aux)
            break
if (ladosT[0] > ladosT[1]-ladosT[2]) and (ladosT[0] < ladosT[1] + ladosT[2]):
    if (ladosT[1] > ladosT[0] - ladosT[2]) and (ladosT[1] < ladosT[0] + ladosT[2]):
        if (ladosT[2] > ladosT[0] - ladosT[1]) and (ladosT[2] < ladosT[0] + ladosT[1]):
            answer = 'podem formar um triângulo'
print('\nAs retas fornecidas', answer)
