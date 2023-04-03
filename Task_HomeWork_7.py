poem = input('Введите стих: ').upper().split()
vowel_letters = {'А', 'О', 'У', 'Ы', 'Э', 'Е', 'Ё', 'И', 'Ю', 'Я'}


def is_rhythm(str):
    list = []
    for word in str:
        count_letter = 0
        for letter in word:
            if letter in vowel_letters:
                count_letter += 1
        list.append(count_letter)
    return len(list) == list.count(list[0])


if is_rhythm(poem):
    print('Парам пам пам')
else:
    print('Пам парам')


def print_operation_table(operation, num_rows=9, num_cols=9):
    for x in range(1, num_rows + 1):
        for y in range(1, num_cols + 1):
            if y == num_cols:
                print(operation(x, y))
            else:
                print(operation(x, y), end='\t')


print_operation_table(lambda x, y: x * y, 5, 5)
