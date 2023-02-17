# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)

# Ввод:
#   0  1  2  3   4   5  6  7   8  9  10 11  12 13  14  15  16 17  18 19
# [-5, 9, 0, 3, -1, -2, 1, 4, -2, 1, -2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# 5
# 15
# Вывод: [1,9,13,14,19]

import random

n = int(input("Введите длину списка: "))
list1 = [random.randint(-5, 15) for i in range(n)]
index = [i for i in range(n)]

print('index =', end="\t")
for i in index:
    print(i, end="\t")

print(end="\n")

print('list1 =', end="\t")
for i in list1:
    print(i, end="\t")

print(end="\n")

min = int(input("Введите min: "))
max = int(input("Введите min: "))

resIndexMinMax = [i for i in range(len(list1)) if list1[i] >= min and list1[i] <= max]

print("resIndexMinMax =", resIndexMinMax)
