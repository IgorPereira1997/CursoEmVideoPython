from random import randint
alunos = []

for i in range(1, 5):
    alunos.append(str(input('Digite o nome do aluno {}: '.format(i))))

print('\nAluno que irá apagar o quadro: {}'.format(alunos.pop(randint(0, 3))))
