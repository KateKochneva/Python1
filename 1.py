# 1/ Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день
# выходным.
#
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

number = int(input('Enter day: '))
if number == 6 or number == 7:
    print("It is weekend")
else:
    print("no weekend")


# 2/ Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
for x in range(2):
    for y in range(2):
        for z in range(2):
            print(x, y, z)
            print(not (x or y or z) == (not x and not y and not z))



# 3/ Напишите программу, которая принимает на вход координаты точки (X и Y),
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка
# (или на какой оси она находится).
#
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

x = int(input('Enter X '))
y = int(input('Enter Y '))

def quarter(x,y):
    a = 4
    if x > 0 and y > 0:
        a = 1
    elif x < 0 and y > 0:
        a = 2
    elif x < 0 and y < 0:
        a = 3
    print(f"The point is in {a} quarters")

quarter(x,y)



# 4/ Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат
# точек в этой четверти (x и y).
# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
#
# Пример:
#
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

def input_numbers(x):
    xy = ["X", "Y"]
    a = []
    for i in range(x):
        number = int(input(f"Enter the coordinate {xy[i]}: "))
        a.append(number)
    return a


def Length(a, b):
    lengthSegment = ((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2) ** (0.5)
    return lengthSegment


print("Enter the coordinate А: ")
pointA = input_numbers(2)
print("Enter the coordinate В: ")
pointB = input_numbers(2)

print(f"Length of the segment: {round(Length(pointA, pointB),2)}")