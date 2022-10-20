def input_check(variants):
    while True:
        try:
            choise = input('> ')
            if choise.isdigit():
                choise = int(choise)
            if choise in variants:
                break
            else:
                print(f'Неверный ввод. доступные варианты: {variants}')
        except:
            print(f'Неверный ввод. доступные варианты: {variants}')
    return choise