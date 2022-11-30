# 1) Вводим с клавиатуры целое число X и У.
# Выводим на экран количество чисел между Х и У, которые делятся на 2 и 3
#
x = int(input("Enter x: "))
y = int(input("Enter y: "))

start = 0
end = 0
if x > y:
    start = y
    end = x
else:
    start = x
    end = y
if end-start != 0:
    for i in range((end-start) -1):
        start += 1
        if start % 2 == 0 or start % 3 == 0:
            print(start)



# 2) Вводим с клавиатуры целое число X
# Далее вводим Х целых чисел.
# Необходимо вывести на экран максимальное и второе максимальное число из введенных чисел.
#

x = int(input("Enter x: "))

lst = []
for i in range(x):
    i = input("Enter: ")
    lst.append(i)

array = list(map(int, lst))

max = 0
min = 0

maxi = array[0]

for ele in array:
    if ele > maxi:
       maxi = ele

print(maxi)
array.remove(maxi)

maxi = array[0]

for ele in array:
    if ele > maxi:
       maxi = ele
print(maxi)



# 3) Вводим с клавиатуры целое число - это зарплата.
# Нужно вывести в консоль -  Минимальное кол-во  купюр, которыми можно выдать ЗП.
# И сколько, и каких бухгалтер выдаст 25 рублевых купюр,  10 рублевых, 3 рублевых и 1 рублевых
#

import math

salary = int(input('Enter salary: '))
count_25 = 0
count_10 = 0
count_3 = 0
count_1 = 0

if (salary > 25):
    count_25 = math.floor(salary / 25)
    salary = salary - 25 * count_25

if (salary > 10):
    count_10 = math.floor(salary / 10)
    salary = salary - 10 * count_10

if (salary > 3):
    count_3 = math.floor(salary / 3)
    salary = salary - 3 * count_3

if (salary > 1):
    count_1 = salary

print('25P: ' + str(count_25))
print('10P: ' + str(count_10))
print('3P: ' + str(count_3))
print('1P: ' + str(count_1))


# 4) Вводим с клавиатуры многозначное число
# Необходимо узнать и сказать последовательность цифр этого числа при просмотре слева направо
# упорядочена по возрастанию или нет.
# Например 1579 - да ( 1 меньше 5, 5 меньше 7, а 7 меньше 9), 1427 - нет

x = int(input())
result = 'no'
while x // 10 != 0:
    x, n = divmod(x, 10)
    if n >= x % 10:
       result = 'yes'
       break
print(result)