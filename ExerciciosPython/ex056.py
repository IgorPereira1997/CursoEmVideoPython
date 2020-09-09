pessoas = [[] for _ in range(3)]
medIdade = 0
homemVelho = 0
qtdMulheres = 0
totPessoas = 4
print()
for i in range(0, totPessoas):
    nome = (str(input('Entre com o nome da pessoa {}: '.format(i + 1))))
    while True:
        idade = (float(input('Entre com a idade da pessoa {}: '.format(i + 1))))
        if idade < 0:
            print('\033[1;31mERRO! Entrada inválida! Tente novamente!\033[m')
        else:
            break
    while True:
        sexo = (str(input('Entre com o sexo da pessoa (M ou F) {}: '.format(i + 1))))
        if sexo != 'M' and sexo != 'F' and sexo != 'm' and sexo != 'f':
            print('\033[1;31mERRO! Entrada inválida! Tente novamente!\033[m')
        else:
            break
    pessoas[0].append(nome)
    pessoas[1].append(idade)
    pessoas[2].append(sexo)
    medIdade += pessoas[1][i]
    if pessoas[2][i] == 'M' or pessoas[2][i] == 'm':
        if i == 0:
            homemVelho = i
        elif pessoas[1][homemVelho] < pessoas[1][i]:
            homemVelho = i
    if pessoas[2][i] == 'F' or pessoas[2][i] == 'f':
        if pessoas[1][i] < 20:
            qtdMulheres = qtdMulheres + 1
    print()

print('Média de idade do grupo: {:.2f}\nHomem mais Velho: {}\nQuantidade de mulheres com menos de 20 anos: {}'
      .format(medIdade/totPessoas, pessoas[0][homemVelho], qtdMulheres))
