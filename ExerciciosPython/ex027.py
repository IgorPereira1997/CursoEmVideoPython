nome = input('Entre com o seu nome completo: ')
nome = nome.split()
i = len(nome)
print('Primeiro nome: {}\nÚltimo nome: {}'.format(nome[0], nome[i-1]))
