while True:
    dist = float(input('\nEntre com a distância da viagem: '))
    if dist < 0:
        print('\nERRO, distância inválida! Tente novamente!')
    else:
        break
print('\nPreço da viagem: R$'+('{:.2f}'.format(dist*0.5) if dist <= 200 else '{:.2f}'.format(dist*0.45)))
