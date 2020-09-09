def validar():
    p = False
    while (not p) or (p < 0):
        try:
            p = float(input('Digite o preço desejado: R$'))
            if p < 0:
                print('Erro, valor digitado é inválido!\n')
        except:
            print('Erro, valor digitado é inválido!\n')
    return p
