# Напишите программу, которая принимает на вход цифру, обозначающую день недели, 
# и проверяет, является ли этот день выходным.    - 6 -> да ,  - 1 -> нет

num = int(input('Введите число: '))
if num == 7 or num == 6:
    print('выходной день')
else:
    print('не выходной день')



# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и 
# выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
# - x=34; y=-30 -> 4,  - x=2; y=4-> 1 , - x=-34; y=-30 -> 3

x = int(input('введите число по координате x '))
y = int(input('введите число по коордитате y '))
if x > 0 and y > 0:
    print('1 четверть')
if x < 0 and y > 0:
    print('2 четверть')
if x < 0 and y < 0:
    print('3 четверть')
if x > 0 and y < 0:
    print('4 четверть')

# Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).

number = int(input('введите число нужной четверти '))

if number == 1:
    print('(x > 0 и y > 0)')
if number == 2:
    print('(x < 0 и y > 0)')
if number == 3:
    print('(x < 0 и y < 0)')
if number == 4:
    print('(x > 0 и y < 0)')


# Напишите программу, которая принимает на вход координаты двух 
# точек и находит расстояние между ними в 2D пространстве.

# - A (3,6); B (2,1) -> 5,09, - A (7,-5); B (1,-1) -> 7,21

x1 = int(input('введите число x1 '))
y1 = int(input('введите число y1 '))
x2 = int(input('введите число x2 '))
y2 = int(input('введите число y2 '))

d = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
print(round(d,3))