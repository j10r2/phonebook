import import_file as imp
import add_person as add
import export_list as exp
import input_check as inp

def magic():
    book = imp.import_file()
    print(book)
    print('выберите действие:\n1 - добавить новый контакт\n2 - экспортировать справочник')
    choise1 = inp.input_check([1, 2])
    if choise1 == 1:
        i = 'y'
        while i == 'y':
            book = add.add_person(book)
            print('добавить следующий контакт?\n y - добавить\n n - выход')
            i = inp.input_check(['y', 'n'])
        exp.export_list(book)
    else:
        exp.export_list(book)