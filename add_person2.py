def add_person2(data_entry):

    enter_data = input("Введите свои данные: ФИО, рабочий телефон и домашний телефон: ")
    import string
    string.punctuation
    for p in string.punctuation:
        if p in enter_data:
            enter_data = enter_data.replace(p, '')
    line1 = enter_data.strip()

    data_entry.append(line1.split())
    return data_entry
