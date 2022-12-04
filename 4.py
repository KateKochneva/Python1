# 1) Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов
# списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
#

n = [2, 3, 5, 9, 3]
sum = 0
for i in range(len(n)):
    if i % 2 == 1:
        sum = sum + n[i]
print(sum)


# 2) Написать программу, которая генерирует двумерный массив на A x B элементов ( A и B вводим с клавиатуры)
# И считаем средне-арифметическое каждой строки (не пользуемся встроенными методами подсчета суммы)
#


N = int(input("enter length of array: "))

a1 = []
b1 = []
for i in range(N):
    new = int(input("a: "))
    a1.append(new)
    new1 = int(input("b: "))
    b1.append(new1)

print(a1)
print(b1)

lst = [a1, b1]
print(lst)

sum = 0
for i in lst:
    for j in i:
        sum = sum + j
    print(sum/(len(a1)))
    sum = 0


# 3) Сгенерируйте список на 30 элементов. Отсортируйте список по возрастанию, методом сортировки выбором.

from random import randint
N = 30
arr = []
for i in range(N):
    arr.append(randint(1, 100))
print(arr)

i = 0
while i < N - 1:
    m = i
    j = i + 1
    while j < N:
        if arr[j] < arr[m]:
            m = j
        j += 1
    arr[i], arr[m] = arr[m], arr[i]
    i += 1

print(arr)
