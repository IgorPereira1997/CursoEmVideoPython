from datetime import datetime

dic = {}
cadastrados = []


def entrar_sexo():
    while True:
        s = str(input('Digite o sexo da pessoa [M/F]: ')).upper()
        if s != 'M' and s != 'F':
            print('\n\033[1;31mERRO! Entrada inválida! Tente novamente!\033[m\n')
        else:
            return s


def entrar_ano(s):
    while True:
        ano = int(input(f'Entre com o ano de {s}: '))
        if s == 'nascimento':
            if datetime.now().year - ano < 0 or datetime.now().year - ano > 100:
                print('\n\033[1;31mERRO! Entrada inválida! Tente novamente!\033[m\n')
            else:
                return ano
        else:
            if dic['ano'] + 18 > ano or ano > datetime.now().year:
                print('\n\033[1;31mERRO! Entrada inválida! Tente novamente!\033[m\n')
            else:
                return ano


def carteira_de_trabalho_valida():
    while True:
        ctps = int(input('Digite o número da CTPS (digite 0 caso não tenha): '))
        if ctps != 0 and (ctps < 9999999 or ctps > 99999999):
            print('\n\033[1;31mERRO! Entrada inválida! Tente novamente!\033[m\n')
        else:
            return ctps


def entrar_sal():
    while True:
        sal = float(input('Digite o salário: R$'))
        if sal <= 998:
            print('\n\033[1;31mERRO! Entrada inválida! Tente novamente!\033[m\n')
        else:
            return sal


def aposenta_quando(nome):
    a = (dic[nome]) + 30
    if a < 0:
        return 0
    else:
        return a


def cadastrar_mais_um():
    op = str(input('\nDeseja cadastrar mais uma pessoa [S/N] ? >>> ')).upper()
    if op != 'S' and op != 'N':
        print('\n\033[1;31mERRO! Entrada inválida! Tente novamente!\033[m\n')
    else:
        return op


while True:
    dic['nome'] = str(input('\nDigite o nome: '))
    dic['ano'] = entrar_ano('nascimento')
    dic['sexo'] = entrar_sexo()
    dic['idade'] = datetime.now().year - dic['ano']
    dic['cpts'] = carteira_de_trabalho_valida()
    if dic['cpts'] != 0:
        dic['ano_contratado'] = entrar_ano('início de contrato')
        dic['salario'] = entrar_sal()
        dic['aposenta'] = aposenta_quando('ano_contratado')
    else:
        dic['ano_contratado'] = 0
    cadastrados.append(dic.copy())
    if cadastrar_mais_um() == 'N':
        break

print()
print('=' * 145)
print(f'{"Informações dos cadastrados":=^145}')
print('=' * 145, '\n')
print(
    f'{"Nome":^32}|{"Sexo":^12}|{"Idade":^12}|{"CPTS":^16}|{"Contratado em":^25}|{"Salário":^20}|{"Aposenta em":^21}|')
print('=' * 145, '\n')
for i in range(0, len(cadastrados)):
    if cadastrados[i]['cpts'] != 0:
        print('{:^32}|{:^12}|{:^12}|{:^16}|{:^25}|{:^20}|{:^21}|'.format(cadastrados[i]['nome'], cadastrados[i]['sexo'],
                                                                         cadastrados[i]['idade'],
                                                                         cadastrados[i]['cpts'],
                                                                         cadastrados[i]['ano_contratado'],
                                                                         round(cadastrados[i]['salario'], 2),
                                                                         'Pode aposentar'
                                                                         if cadastrados[i]['aposenta'] == 0
                                                                         else 'Não pode aposentar'))
    else:
        print(f'{cadastrados[i]["nome"]:^32}|{cadastrados[i]["sexo"]:^12}|{cadastrados[i]["idade"]:^12}|'
              f'{"Não tem vínculo empregatício":^85}|')
