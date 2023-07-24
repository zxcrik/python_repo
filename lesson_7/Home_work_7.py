    ### Easy A ###
# print("Числовой ряд")
# num_1 = int(input("Введите первое число: "))
# num_2 = int(input("Введите второе число: "))

# if num_1 < num_2:
#     for i in range(num_1 , num_2 + 1):
#         print(i, end = " ") 

# if num_1 > num_2:
#     for j in range(num_1 , num_2 - 1, -1):
#         print(j, end = " ")

# if num_1 == num_2:
#     print(num_1)

    ### Easy B ###
# print("Числовой ряд")
# a = int(input("Введите первое число: "))
# b = int(input("Введите второе число: "))

# for i in range(a - int(a % 2 == 0),b - 1 ,-2):
#     print(i, end = " ")

    ### Medium A ###
# print("Пробежка")
# a = int(input("Введите первое число: "))
# b = int(input("Введите второе число: "))
# c = int(input("Введите третье число: "))
# d = int(input("Введите четвертое число: "))
# check = False

# for i in range(a, b+1):
#     if i % d == c:
#         print(i, end = " ")
#         check = True
# if check = False:
#     print("таких чисел нет")
    ### Medium B ###
# print("Четный элемент")
# num = int(input("Введите количество чисел: "))
# summ = 0

# for i in range(num):
#     a = int(input("Введите число: "))
#     summ += a
# print("Сумма чисел: ",summ)

    ### Hard A ###
# print("Больше предыдущего")
# from random import randint
# x = randint(1,15)
# y = randint(1,15)                                         
# print("Сумма загаданных чисел: ",s := x + y)
# print("Произведение загаданных чисел: ",p := x * y)
# for n1 in range(0,16):
#     for n2 in range(0,16):
#         if n1 + n2 == s and n1 * n2 == p:
#             print("x =",n1,"y =",n2 )

    ### Hard B ###
# print("Второй max")
# a = int(input("Введите первый коэфицент: "))
# b = int(input("Введите второй коэфицент: "))
# c = int(input("Введите третий коэфицент: "))
# d = int(input("Введите четвертый коэфицент: "))
# check = False

# for x in range(-100,101):
#     if a * (x ** 3) + b * (x ** 2) + c * x  + d == 0:
#         print("x =",x)
#         check = True
# if not check: 
#     print("x не найден!")
