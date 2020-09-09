nome = str(input('\nDigite o nome compelto da pessoa: '))
nomeSeparado = nome.split()

print("""\nNome com tudo maiúsculo: {}
Nome com tudo minúsculo: {}         
Quantidade de letras: {}
Quantas letras tem o primero nome: {}""".format(nome.upper(), nome.lower(), len(nome.strip()), len(nomeSeparado[0])))
