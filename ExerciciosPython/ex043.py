peso = 0
alt = 0

while True:
    peso = float(input('Entre com o seu peso: '))
    if peso < 0:
        print('\033[1;31mERRO! Peso inválido!\033[m')
    else:
        break

while True:
    alt = float(input('Entre com a sua altura: '))
    if alt < 0:
        print('\033[1;31mERRO! Altura inválida!\033[m')
    else:
        break
print()
if (peso / (alt**2)) < 18.5:
    print('Você está \033[1;31mABAIXO DO PESO\033[m')
elif (peso / (alt**2)) < 25:
    print('Você está com \033[1;32mPESO IDEAL\033[m')
elif (peso / (alt**2)) < 30:
    print('Você está com \033[1;33mSOBREPESO\033[m')
elif (peso / (alt**2)) < 40:
    print('Você está com \033[1;34mOBESIDADE\033[m')
else:
    print('Você está com \033[1;35mOBESIDADE MÓRBIDA\033[m')
