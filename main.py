monets = int(input('Количество монет'))
count_orel = 0
count_reshko = 0
for _ in range(monets):
    x = int(input('Орел-1 / Решко-0'))
    if (x == 1):
        count_orel += 1
    else:
        count_reshko += 1
print()

