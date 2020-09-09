def main():
    print()
    while True:
        print('\033[1;46m', '='*40, '\033[m')
        print(f'\033[1;46m{"Sistema de ajuda PyHelp":^42}\033[m')
        print('\033[1;46m', '=' * 40, '\033[m')
        func = input('\n\033[1;33mDigite o comando a ser analisado (digite FIM para finalizar) >>> \033[m')
        if func == 'FIM':
            print('\n\033[1;31mFinalizando programa....\033[m\n')
            break
        else:
            help(func)


if __name__ == '__main__':
    main()
