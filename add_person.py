import input_check as inp
def add_person(data_entry):
    print('выберите вариант ввода:\n1 - построчно\n2 - одной строкой через разделитель')
    if inp.input_check([1, 2]) == 1:
        surname = input("Фамилия: ")
        name = input("Имя: ")
        patronymic = input("Отчество: ")
        home_phone  = input("Домашний телефон: ")
        work_phone = input("Рабочий телефон: ")
        heading = [surname, name, patronymic, home_phone, work_phone]
        data_entry.append(heading)
    else:
        enter_data = input(
            "Введите данные через разделитель (фамилия, имя, отчество, рабочий телефон, домашний телефон): ")
        import string
        for p in string.punctuation:
            if p in enter_data:
                enter_data = enter_data.replace(p, ' ')
        data_entry.append(enter_data.strip().split())
    return data_entry
