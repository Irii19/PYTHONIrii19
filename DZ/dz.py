# for i in range(number):
#     n = i + i
#     print((i+1)*(n), end=' ')

# # Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# # - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]

# def fib(n):
#     if n in [1, 2]:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)

# list = []
# for e in range(2, 8):
#     list.append(fib(e))
# print(list)   # 1 1 2 3 5 8 13 ...

# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10


n = int(input("Введите число: "))
s = ""
while n != 0:
    s = str(n%2) + s
    n //=2
print(s)