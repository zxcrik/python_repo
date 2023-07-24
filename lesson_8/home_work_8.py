    ### Easy A ###
# import math
# a = int(input("Введите a: "))   # a не должно равняться 0
# b = int(input("Введите b: "))

# for i in range(a,b+1):
#     if i % math.sqrt(i) == 0:
#         print(i, end = " ")

    ### Easy B ###
# x = int(input("Введите число: "))
# i = 0
# a = [] 

# for j in range(1,x+1):
#     if x % j == 0:
#         a.append(j)
#     if x % j != 0:
#         j += 1
# print(a)

    ### Medium A ###
# a = int(input("Введите количество чисел: "))
# num = 0
# c = 0

# for num in range(a):
#     num = int(input("Введите число: "))
#     if num == 0:
#         c += 1

# if c > 0:
#     print("yes")
# else:
#     print("no")

    ### Medium B ###
# p = int(input("Введите количество чисел: "))
# num = 0
# a = 0
# b = 0
# c = 0

# for num in range(p):
#     num = int(input("Введите число: "))
#     if num == 0:
#         a += 1
#     if num > 0:
#         b += 1
#     if num < 0:
#         c += 1 
# print("Число нулей: ",a)
# print("Положительных чисел: ",b)
# print("Отрицательных чисел: ",c)

    ### Hard A ###
# x = int(input("Введите число: "))

# for i in range(1, x + 1):
#     for j in range(1, i + 1):
#         print(j, end =" ")
#     print()

    ### 2 - ой способ решения программы ###
# n = int(input("Введите число: "))
# text = ""

# for i in range(1, n + 1):
#     text += str(i)
#     print(text, end = " ")

    ### Hard B ###
# n = int(input("Введите число: "))
# summa = 0

# for i in range(1, n + 1):
#     summa += i
#
# for i in range(n - 1):
#     summa -= int(input("Введите значение оставшийся карточки: "))
# print(summa) 