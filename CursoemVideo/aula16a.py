lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')

# Tuplas são imutáveis

for comida in lanche:
    print(f'Eu vou comer {comida}')
print('Comi pra caramba!')
print(len(lanche))

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')

print(sorted(lanche))

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c)

del()