# 1. Последовательностью Фибоначчи называется последовательность чисел a0, a1, ..., an, ..., где
#
# a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
#
# Требуется найти N-е число Фибоначчи

# 0, 1, 1, 2, 3, 5, 8, 13...


# Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на максимальные.
# Напишите программу, которая заменяет оценки Василия, но наоборот: все максимальные – на минимальные.

# Напишите функцию, которая принимает одно число и проверяет, является ли оно простым

#
# def fibonachi_recursion(serial_number):
#     if serial_number == 1:
#         return 1
#     if serial_number == 2:
#         return 1
#     return fibonachi_recursion(serial_number - 1) + fibonachi_recursion(serial_number - 2)
#
#
# def fibonachi_iteration(serial_number):
#     first = 0
#     second = 1
#     if serial_number == 1:
#         return first
#     if serial_number == 2:
#         return second
#     count = 2
#     while serial_number != count:
#         third = first + second
#         first = second
#         second = third
#         count += 1
#         return third


# print(fibonachi_recursion(8))

# import random
#
#
# def a(input_list):
#     input_list.append(1.9)
#     result_temp = []
#     result = []
#     for i in range(len(input_list) - 1):
#         if input_list[i] == input_list[i + 1] - 1:
#             result_temp.append(input_list[i])
#         else:
#             if input_list[i] not in result_temp:
#                 result_temp.append(input_list[i])
#             result.append(result_temp)
#             result_temp = []
#
#     print(result)
#     result_str = []
#     for i in result:
#         if len(i) >= 2:
#             result_str.append(f"{i[0]}-{i[-1]}")
#         else:
#             result_str.append(f"{i[0]}")
#     return result_str
#
#
# input_list = sorted(set([random.randint(1, 10) for _ in range(10)]))
#
# print(input_list)
# print(*a(input_list), sep=',')

# def cross(mas_1, mas_2):
#     second_set = set(mas_2)
#     r = []
#     for i in mas_1:
#         if i not in second_set:
#             r.append(i)
#     return r
#
#
# mas1 = int(input('размер 1 массива'))
#
# first_mas = []
# for i in range(mas1):
#     first_mas.append(input(f'{i + 1} элемент масива'))
#
# mas2 = int(input('размер 2 массива'))
# second_mas = []
# for i in range(mas2):
#     second_mas.append(input(f'{i + 1} элемент масива'))
#
# print(cross(first_mas,  second_mas))


# def count_correct_max(input_arr: list):
#     count = 0
#     for i in range(1, len(input_arr) - 1):
#         if input_arr[i - 1] < input_arr[i] > input_arr[i + 1]:
#             count += 1
#             return count
#
# len_array = int(input("Введите длинну масива: "))
# array = []
# for i in range(len_array):
#     array.append(input(f"Введите {i + 1}-й элемент массива: "))
#
# print(array)
# print(count_correct_max(array))


import random


# def count_couple(input_arr: list):
#     find_couple = 0
#     number_dict = {}
#     for i in input_arr:
#         if i not in number_dict:
#             number_dict[i] = 1
#         else:
#             number_dict[i] += 1
#     for i in number_dict.values():
#         find_couple += i // 2
#     return find_couple
#
# array = [random.randint(1, 20) for _ in range(10)]
# print(array)
# print(count_couple(array))


def sum_of_divisors(input_number: int):
    sum_result = 0
    for i in range(1, input_number // 2 + 1):
        if input_number % i == 0:
            sum_result += i
    return sum_result


def friendly_numbers(input_num: int):
    find = set()
    for i in range(1, input_num + 1):  # i = 220
        sum_temp_number = sum_of_divisors(i)  # 284
        sum2 = sum_of_divisors(sum_temp_number)
        if sum2 == i and sum_temp_number != i and i not in find and sum_temp_number not in find:
            print(sum_temp_number, i)
            find.add(i)


input_k = int(input("Введите число k: "))
friendly_numbers(input_k)


def rle(some_str):
    res_list = []

    some_str += ' '
    temp_letter = some_str[0]
    count_letter = 1
    for ind in range(1, len(some_str)):
        if some_str[ind] == temp_letter:
            count_letter += 1
        else:
            if count_letter == 1:
                res_list.append(f'{temp_letter}')
            else:
                res_list.append(f'{temp_letter}{count_letter}')
            count_letter = 1
            temp_letter = some_str[ind]
    print(res_list)
    print(*res_list, sep='')


rle('AAAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBB')


def rle(st):
    new_list = []
    new_list = st[0]

    count_l = 1
    for i in range(1, len(st)):
        if st[i] == new_list:
            count_l += 1
        else:
            new_list

rle('AAAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBB')

