
def export_list(any_list, format_var):
    if format_var == 1:
        file = 'file.csv'
    elif format_var == 2:
        file = 'file.txt'
    with open(file, 'w') as text:
        for i in any_list:
            text.write(":".join(i)+'\n')
    
