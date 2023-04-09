def add_date():
    last_name = input('Введите фамилию')
    first_name = input('Введите имя')
    phone = input('Введите телефон')
    with open('SQL.txt', 'a', encoding='utf-8') as file:
        file.write(f'{last_name} {first_name} {phone}\n')


def show_date():
    with open('SQL.txt', 'r', encoding='utf-8') as file:
        print('========================================')
        print(file.read())
        print('========================================')


def search_date(search_str):
    count_str = 0

    print('========================================')
    with open('SQL.txt', 'r', encoding='utf-8') as file:
        for line in file:
            line = line.split()
            for word in line:
                if word.lower() == search_str.lower():
                    print(*line)
                    count_str += 1
    if count_str == 0:
        print('Записей не найдено')
    else:
        print(f'\nНайдено {count_str} записей')
    print('========================================')
    return count_str


def delete_date(delete_str):
    if search_date(delete_str) == 0:
        print('Удалять нечего')
    else:
        lists = []
        with open('SQL.txt', 'r', encoding='utf-8') as file:
            for line in file:
                line = line.split()
                lists.append(line)

        with open('SQL.txt', 'w', encoding='utf-8') as files:
            for line in lists:
                for word in line:
                    if word.lower() == delete_str.lower():
                        break
                else:
                    files.write(' '.join(line) + '\n')
        print('Запись удалена\n')


def update_data():
    update_str_old = input('Введете имя, фамилию или телефон юзера, которого хотите изменить')

    if search_date(update_str_old) == 0:
        print('Изменять нечего\n')
    else:
        update_str_new = input(' Навая фамилия, имя и телефон').split()

        lists = []
        with open('SQL.txt', 'r', encoding='utf-8') as file:
            for line in file:
                line = line.split()
                lists.append(line)

        with open('SQL.txt', 'w', encoding='utf-8') as files:
            for line in lists:
                for word in line:
                    if word.lower() == update_str_old.lower():
                        files.write(' '.join(update_str_new) + '\n')
                        break
                else:
                    files.write(' '.join(line) + '\n')
        print('Запись успешно обновлена')
