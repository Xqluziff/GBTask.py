import DefFile as df

while True:
    num = input('Выберите действие с файлом\n'
                '1 - запись\n'
                '2 - чтение\n'
                '3 - поиск\n'
                '4 - удаление\n'
                '5 - обновить')
    if num == '1':
        df.add_date()
    elif num == '2':
        df.show_date()
    elif num == '3':
        find_str = input('Введите имя, фамилию или телефон: ')
        df.search_date(find_str)
    elif num == '4':
        del_str = input('Введете имя, фамилию или телефон для удаления')
        df.delete_date(del_str)
    elif num == '5':
        df.update_data()
    else:
        break









