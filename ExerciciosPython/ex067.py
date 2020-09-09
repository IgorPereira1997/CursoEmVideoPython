
while True:
    print('\n=====================================')
    n = int(input('Deseja ver a tabuada de qual número? '))
    if n < 0:
        break
    for i in range(1, 11):
        print(f'{n:>2} X {i:>2} = {n*i:>3}')
    print('\n=====================================')
