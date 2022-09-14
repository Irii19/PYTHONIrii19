
#  поиск  похожего 

# ВАРИАНТ 1

# list = ['222anton435', ' alnitlo', "00000000a000000n0000t", 'ant0n']
# print(list)
# for i in list:
#     if 'a' in i:
#         if 'n' in i:
#             if "t" in i:
#                 if 'o' in i:
#                     if 'n' in i:
#                         print(list.index(i)+1)

# ВАРИАНТ 2

# n = int(input())
# list1 = []
# for i in range(n):
#     a = input()
#     if 'a' in a:
#         a = a[a.find('a'):]
#         if 'n' in a:
#             a = a[a.find('n'):]
#             if 't' in a:
#                 a = a[a.find('t'):]
#                 if 'o' in a:
#                     a = a[a.find('o'):]
#                     if 'n' in a:
#                         list1.append(i + 1)
# print(*list1)

# ПОИСК НАИБОЛЬШЕГО КОЛИЧЕСТВА ПОВТОРЕНИЙ "орел и решка"

# s=input()
# t=0
# while "Р"*(t+1) in s:
#     t+=1
# if t!=0:
#         print(t)
# else:
#     print(0)




# # 2. 1. Напишите программу, которая принимает на вход число N и выдаёт 
# # последовательность из N членов.- Для N = 5: 1, -3, 9, -27, 81

# N = int(input('введите число '))
# for i in range(N):
#     print((-3)**i, end=', ')




# # 2. 3. Напишите программу, в которой пользователь будет задавать две строки,
# # а программа - определять количество вхождений одной строки в другой

# stritg1 = input()
# string2 = input()

# if stritg1 > string2:
#     print(stritg1.count(string2))
# else:
#     print(string2.count(stritg1))



a = 'pyt'
b = 'pythonpythonpython'
count = 0
for i in range(0, len(b) - len(a)):
    if b[i:i + len(a)] == a:
        count += 1
print(count)