flag = True
num = int(input('\nDigite um número para verificação se é primo ou não: '))

for i in range(2, num):
    if num % i == 0:
        flag = False
        break
print('O número {} '.format(num)+('é primo!' if flag else 'não é primo!'))
