



monets = int(input('Количество монет: '))
count_orel = 0
count_reshko = 0
for _ in range(monets):
    x = int(input('Орел-1 / Решко-0: '))
    if(x == 1):
        count_orel += 1
    else:
        count_reshko += 1
if(count_reshko < count_orel):
    print(f'Переверни решки {count_reshko} раз')
else:
    print(f'Переверни орла {count_orel} раз')

    #------------------------------------

x = int(input('Загазай число 1: '))
y = int(input('Загазай число 2: '))
for i in range(x+1):
    for j in range(y+1):
        if x + y == i + j and x * y == i * j:
            print(i, j)

    #_________________________________
n = int(input('Введи число'))
i = 0
while 2 ** i <= n:
    print(2 ** i)
    i += 1




