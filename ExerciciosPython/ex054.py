from datetime import datetime

totPerson = 7
maior = 0
print()
for i in range(1, totPerson + 1):
    n = int(input('Digite o ano de nascimento da pessoa {}: '.format(i)))
    if datetime.now().year - n >= 18:
        maior = maior + 1
print('\nPessoas que atingiram a maioridade: {}\nPessoas que não atingiram a maioridade: {}'
      .format(maior, totPerson-maior))
