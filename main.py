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








