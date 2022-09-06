# print('hello world')
# print('hello world')
# Типы данных справедливы int, float, boolean, str, list, None и др.



# ТИП ДАННЫХ И ИХ ВЫВОД

# f = True
# g = False
# print(f)    #t  True
# print(g)    #t  False

# a = 123
# b = 1.23
# print(a)    #t   123
# print(b)    #t   1.23
# value = 12345
# print(value)    #t   12345

# s = 'Hello World'
# print(s)    #t  Hello World

# list = []
# list1 = [1, 2, 3]
# list2 = ['1', '2', 'Hello', 1,2, 3,4.5, 6, 6.7,True]
# print(list)     #t  []
# print(list1)    #t  [1, 2, 3]
# print(list2)    #t  ['1', '2', 'Hello', 1, 2, 3, 4.5, 6, 6.7, True]

# value   # если ввести переменнную в начале для её дольнейшего использоваия дальше 
#         # по программе без присваения значения (None), то произойдет ошибка.
# a = 123
# b = 1.23
# print(a)
# print(b)
# value = 12345
# print(value)    #t  ошибка NameError: name 'value' is not defined. Did you mean: 'False'?

# value = None
# a = 123
# b = 1.23
# print(a)    #t  123
# print(b)    #t  1.23
# value = 12345
# print(value)    #t  12345




# Распознаваемые escape-последовательности:

# \newline - Обратная косая черта и новая строка игнорируются.
# \\ - Обратная косая черта (\).
# \' - Одинарная кавычка (').
# \" - Двойная кавычка (").
# \a - ASCII Bell (BEL).
# \b - ASCII Backspace (BS).
# \f - ASCII Formfeed (FF).
# \n - переход на новую строку .
# \r - Возврат каретки ASCII (CR).
# \t - Горизонтальная вкладка ASCII (TAB).
# \v - Вертикальная вкладка ASCII (VT)

#  ВЫВОД  КЛАССА ВВОДИМЫХ ДАНННЫХ

# value = None
# print()     #t  пустая строка
# print(type(value))  #t  <class 'NoneType'> позже класс значения измениться
#                     #   на тот который уму присвоется
# print()     #t  пустая строка
# a = 123
# b = 1.23
# s = 'Hello World'
# print(s)    #t  Hello World
# print(type(s))  #t  <class 'str'>
# print(type(a))    #t  <class 'int'>
# print(type(b))    #t  <class 'float'>
# value = 12345
# print(type(value))    #t  <class 'int'>


# ИНТРОПОЛЯЦИЯ

# a = 123
# b = 1.23
# value = 12345
# s = 'Hello World'
# print(a, b, s)  #t  123 1.23 Hello World
# print(type(s), b, s)    #t  <class 'str'> 1.23 Hello World
# print(a, '-', value, "-", s)    #t  123 - 12345 - Hello World
# print(f'{b} - {value} - {s}')     #t  1.23 - 12345 - Hello World


# ФОРМАТИРОВАНИЕ

# a = 123
# b = 1.23
# value = 12345
# s = 'Hello World'
# print('{} - {} - {}'.format(b, value, s))   #t  1.23 - 12345 - Hello World
# print()
# print('{1} - {2} - {0}'.format(b, value, s))    #   перестовление выводимых данных '{1} - {2} - {0}'.format(b, value, s)
#                                                 #t  12345 - Hello World - 1.23
# print()
# print(f'{b} - {value} - {s}')   #   интрополяция
#                                 #t   1.23 - 12345 - Hello World



# ВЫВОД И ВВОД ДАННЫХ

# print('введите a')
# a = input()
# print('введите b')
# b = input()
# print(a, b)
# print('{} {}'.format(a, b))
# print(f'{a} {b}')
# print(a, '+', b, '=', a+b)  # по умолчанию раюотают в формате строки
#                             #t  30 + 40 = 3040

#  ДЛЯ ЦЕЛЫХ ЧИСЕЛ

# print('введите a')
# a = int(input())
# print('введите b')
# b = int(input())
# print(a, '+', b, '=', a+b)  #t  2 + 4 = 6

#   ДЛЯ ВЕЩЕСТВЕХЫХ ЦИСЕЛ (ЧИСЕЛ С ПЛАВУЮЩЕЙ ЗАПЯТОЙ)

# print('введите a')
# a = float(input())
# print('введите b')
# b = float(input())
# print(a, '+', b, '=', a+b)  #t  55.5 + 55 = 110.5



# АРИФМЕТИЧЕСКИЕ ОПЕРАЦИИ

# +, -, *, /, %, /, ** Приоритет операций
# **, ⊕, ⊖, *, /, /, %, +, -
# ( )   Скобки меняют приоритет
# сокращённые операции
 
# a = + 123
# b = - 321
# c = a - b
# print(c)    #t  444

# a = 123
# b = - 321
# c = a + b
# print(c)    #t  -198

# a =  4
# b = -6
# c = a * b
# print(c)    #t  -24

# a = -4
# b = 6
# c = a / b
# print(c)    #t  -0.6666666666666666

# a = -11
# b = 6
# c = a // b
# print(c)    #t  -2

# a = 11
# b = 6
# c = a // b  #t  получение целого числа при делении
# print(c)    #t  1

# a = 16
# b = 6
# c = a % b   #t  остаток от деления
# print(c)    #t  4

# a = 2
# b = 8
# c = a ** b  #   возведение в степень
# print(c)    #t  256

# a = 1,3
# b = 3
# c = a * b  #   умножение с запятой (,) в место точки (.)
# print(c)    #t  (1, 3, 1, 3, 1, 3)

# a = 1.2
# b = 3
# c = a * b  #   умножение с вещественными числами
# print(c)    #t  3.5999999999999996

# a = 1.31231223
# b = 3
# # c = round(a * b)  #   умножение с вещественными числами c функцией (round) без аргументов
# c = round(a * b, 5)  #   умножение с вещественными числами c функцией (round) без аргументов
#                        #t   3.6
# print(c)    #t  3.93694

# a = 3
# a += 5
# print(a)



# ЛОГИЧЕСКИЕ ОПЕРАЦИИ

# >, >=, <, <=, ==, !=
# not, and, or – не путать с &, |, ^ 
# Кое-что ещё: is, is not, in, not in
# gen

# a = 1 > 4
# print(a)    #t  False

# a = 1 < 4
# print(a)    #t  True

# a = 1 < 4 and 5 > 2
# print(a)    #t  True

# a = 1 == 2
# print(a)    #t  False

# a = 1 != 2
# print(a)    #t  True

# a = 'qwe'
# b = 'qwe'
# print(a == b)    #t  True

# a = [1, 2]
# b = [1, 3]
# print(a == b)    #t  False

# a = 1 < 3 < 5
# print(a)    #t  True

# tunc = 1
# T = 4
# x = 123
# print(tunc<T>x)    #t  False

# f = 1 > 2 or 4 < 6  # or = или
# print(f)    #t  True

# f = [1, 2, 3, 4]
# print(f)    #t  [1, 2, 3, 4]
# print(2 in f)   # in = в
#                 #t  True

# f = [1, 2, 3, 4]
# print(f)    #t  [1, 2, 3, 4]
# print(not 2 in f)   # in = в
#                     #t  False

# f = [1, 2, 3, 4]
# is_ood = f[0] % 2 == 0
# print(is_ood)    #t  False

# f = [1, 2, 3, 4]
# is_ood = not f[0] % 2
# print(is_ood)    #t  False



# УПРАВЛЯЮЩИЕ КОНСТРУКЦИИ

#  if, if-else

# a = int(input('a = '))
# b = int(input('b = '))
# if a > b:
#     print('большее число ', a)
# else:
#     print('большее число ', b)

# username = input('введите имя: ')
# if username == 'Маша':
#     print(' УРА, это же МАША')
# elif username == 'Мариина':
#     print(' Я так ждала Вас, Марина!')
# elif username == 'Ильнар':
#     print('Ильнар - топ')
# else:
#     print('Привет, ', username)

# while

# original = 23
# inverted = 0
# while original != 0:
#     inverted = inverted * 10 + (original % 10)
#     original //= 10
#     print(original)
# else:
#     print('пожалуй \nхватит')
# print(inverted)

# for

# for i in 1,2,3,4,5:
#     print(i**2)   #t  1 4 9 16 25

# list = [1,6,2,3,4,10,5]
# for i in list:
#     print(i)   #t  1 6 2 3 4 10 5

# for i in range(5):
#     print(i)   #t  0 1 2 3 4

# for i in range(1, 5):
#     print(i)   #t  1 2 3 4

# for i in range(1, 10, 2):
#     print(i)   #t  1 3 5 7 9

# for i in 'qwerty':
#     print(i)   #t  q w e r t y



# НЕМНОГО О СТРОКАХ

# text = 'съешь ещё этих мягких французских булок'

# print(len(text))  #   39      количество символов
# print('ещё' in text)  #   True     наличие подстроки
# print(text.isdigit()) #   False   являются ли все символы числами
# print(text.islower()) #   True    являются ли все символы нижнего регистра
# print(text.replace('ещё','ЕЩЁ'))    # замена

# for c in text:        
# print(c)

# help(str)   #   встроеная справка языка PYTHON
#             # для выхода нажать "q"

# СРЕЗЫ

# text = 'съешь ещё этих мягких французских булок' 
# print(text[0])    # c
# print(text[1])    # ъ
# print(text[len(text)-1]) # к 
# print(text[-5]) # б 
# print(text[:])    # print(text) 
# print(text[:2]) # съ 
# print(text[len(text)-2:]) # ок 
# print(text[2:9]) # ешь ещё
# print(text[6:-18]) # ещё этих мягких 
# print(text[0:len(text):6]) # сеикакл 
# print(text[::6]) # сеикакл
# text = text[2:9] + text[-5] + text[:2] # ...



# СПИСКИ. Список – пронумерованная, изменяемая коллекция объектов произвольных типов

# numbers = [1, 2, 3, 4, 5]
# print(numbers)           #   [1, 2, 3, 4, 5]

# numbers = list(range(1, 6)) 
# print(numbers)           #   [1, 2, 3, 4, 5]

# numbers[0] = 10
# print(f'{len(numbers)} len')
# print(numbers)          #   [10, 2, 3, 4, 5]
# for i in numbers: i *= 2
# print(i)            #   [20,  4,  6,  8,  10]
# print(numbers)          #   [10,  2,  3,  4,  5]

# colors = ['red', 'green', 'blue'] 
# for e in colors:
#     print(e)      #    red green blue

# for e in colors:
#     print(e*2)    #    redred greengreen blueblue

# colors.append('gray')   #   добавить в конец
# print(colors == ['red', 'green', 'blue', 'gray'])    #  True colors.remove('red') #del colors[0] # удалить элемент
# colors.remove('red')
# del colors[0]

def f(x):
    if x == 1:
        return 'Целое' 
    elif x == 2.3:
        return 23 
    else:
        return

arg = 1
print(f(arg))
print(type(f(arg)))

