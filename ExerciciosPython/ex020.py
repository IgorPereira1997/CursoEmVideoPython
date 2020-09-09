from random import randint

alunos = []
i = 0

for i in range(1, 5):
    alunos.append(str(input('Digite o nome do aluno {}: '.format(i))))

--i

for j in range(1, 5):
    if j == 1:
        print('znOrdem de apresentação dos alunos', end=' >>>\n')
    print('Aluno {}: {}'.format(j, alunos.pop(randint(0, --i))))

