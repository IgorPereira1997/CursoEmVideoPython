exp = input('Entre com a sua expressão numérica: ')

if exp.find('(') != -1 and exp.find(')') != -1:
    print('A sua expressão está '+('correta.' if exp.count('(') == exp.count(')') else 'errada.'))
else:
    print('Sua expressão não tem parênteses, logo está correta')
