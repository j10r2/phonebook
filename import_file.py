import input_check as inp
def import_file():
    while True:
        try:
            file_name = input('введите название файла, из которого считываем данные (с расширением):\n')
            return list(map(lambda i: i.split(':'), open(file_name, encoding='utf-8').read().split('\n')))
        except:
            print('файл не найден, выберите действие: \n 1 - выбрать другой файл \n 2 - выйти из программы')
            if inp.input_check([1, 2]) == 2:
                exit()
