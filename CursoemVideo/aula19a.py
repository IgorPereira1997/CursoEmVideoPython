pessoas = {'nome': 'Igor', 'sexo': 'M', 'idade' : 22}
del pessoas['sexo']
pessoas['nome'] = 'Dan'
pessoas['peso'] = 98.5
print(pessoas['nome'])
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())

for k in pessoas.keys():
    print(k)

for k, v in pessoas.items():
    print(f'{k} = {v}')
