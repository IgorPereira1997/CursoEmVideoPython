from random import randint

maior, menor = 0, 0

tupla = (randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100),
         randint(0, 100))
print()
print(tupla)

for i in range(0, len(tupla)):
    if i == 0:
        maior = menor = tupla[i]
    elif maior < tupla[i]:
        maior = tupla[i]
    elif menor > tupla[i]:
        menor = tupla[i]

print(f'Maior valor: {maior}\nMenor valor: {menor}')
