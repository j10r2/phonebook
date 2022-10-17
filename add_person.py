def add_person(data_entry):
    global heading
    surname = input("Фамилия: ")
    name = input("Имя: ")
    patronymic = input("Отчество: ")
    home_phone  = input("Домашний телефон: ")
    work_phone = input("Рабочий телефон: ")
    heading = [surname, name, patronymic, home_phone, work_phone]
    data_entry.append(heading)
    return data_entry
