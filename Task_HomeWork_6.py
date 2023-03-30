from random import randint

a1 = int(input("Введите значение 1-го элемента:"))
d = int(input("Введите разность элементов:"))
n = int(input("Введите количество элементов:"))

res = []  # [a1 + (i - 1) * d for i in range(1, n + 1)]
for i in range(1, n + 1):
    res.append(a1 + (i - 1) * d)
print(res)



min = int(input('мин число'))
max = int(input('max число'))

l = []
for i in range(10):
    l.append(randint(1, 10))
print(l)
res = []
for i in range(10):
    if min <= l[i] <= max:
        res.append(i)
print(res)
