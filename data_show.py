def show_list(book, index, parameter):
    text = ''
    new_book = []
    for i in range(len(book)):
        if book[i][index] == parameter:
            new_book.append(book[i])
    for i in range(0, len(new_book)):
        separator = '\n'
        text = text+' '.join(new_book[i])+separator
    print(text)