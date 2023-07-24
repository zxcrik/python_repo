 
    ### Easy A ###
# i = 0
# j = 0

# for i in range(1,100):
#     i += 1
#     print(i, 100 - i, sep = " ----- ")


    ### Easy B ###
# n = int(input('Введите число = '))
# import math
# f = math.factorial(n)
# print(n,'! = ', f)

    ### Easy C ###
# n = int(input("Введите кол-во звезд: "))

# for i in range(n):
#     for j in range(i + 1):
#         print("*", end = " ")
#     print()

    ### Easy D ###
# n = int(input("Введите кол-во чисел: "))
# s = 0

# for i in range(n):
#     num = int(input("введите число: "))
#     if num % 10 == 8:
#         s += 1
# print(s)

    ### Medium A ###
# c = int(input("Введите число: "))
#
# for x in range(1, c + 1):
#     print(" " * (c - x) + '#' * x)

    ### Medium B ###
# a = int(input("Введите наименьшее число: "))
# b = int(input("Введите наибольшее число: "))
# summa = 0

# for i in range(a, b+1):
#     summa += i
# print(summa)

    ### Hard B ###
# n = int(input("n= "))
# lst = []
# k = 0

# for i in range(2, n + 1):
#     for j in range(2, i):
#         if i % j == 0:
#             k = k + 1
#     if k == 0:
#         lst.append(i)
#     else:
#         k = 0

# print(lst)