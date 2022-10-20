import input_check as inp
def export_list(book):
    print('выберите формат экспорта:\n    1 - csv\n    2 - txt')
    format_var = inp.input_check([1, 2])
    if format_var == 1:
        file = 'phonebook.csv'
    else:
        file = 'phonebook.txt'
    with open(file, 'w', encoding='utf-8') as text:
        end = '\n'
        for i in range(len(book)):
            if i == len(book)-1:
                end = ''
            text.write(":".join(book[i])+end)
