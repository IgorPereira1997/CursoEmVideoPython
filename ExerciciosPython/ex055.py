peso = []
totPessoas = 5
print()
for i in range(1, totPessoas + 1):
    peso.append(float(input('Entre com o peso da pessoa {}: '.format(i))))
peso.sort()
print('\nMaior peso dos fornecidos: {:.2f}kg\nMenor peso dos fornecidos: {:.2f}kg'
      .format(peso.pop(totPessoas-1), peso.pop(0)))
