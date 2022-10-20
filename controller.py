import import_file as imp
import add_person as add
import export_list as exp
import input_check as inp
import data_show as shw

def magic():
    book = imp.import_file()
    j = 'y'
    while j == 'y':
        print('выберите действие:\n1 - добавить новый контакт\n2 - найти контакт\n3 - экспортировать справочник')
        choise = inp.input_check([1, 2, 3])
        if choise == 1:
            i = 'y'
            while i == 'y':
                book = add.add_person(book)
                print('добавить следующий контакт?\n y - добавить\n n - выход')
                i = inp.input_check(['y', 'n'])
        elif choise == 2:
            print('выберите параметр поиска:\n 1 - фамилия\n 2 - имя\n 3 - отчество\n 4 - моб. телефон\n 5 - дом. телефон')
            choise1 = inp.input_check(range(1, 6))-1
            search_text = input('введите искомое значение: >')
            shw.show_list(book,choise1,search_text)
        else:
            exp.export_list(book)
        print('продолжить работу?: \n 1 - продолжить \n 2 - закрыть справочник')
        if inp.input_check([1, 2]) == 2:
            exit()