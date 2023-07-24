    ### Easy A ###
# from math import *
# a = int(input("Введите первое число: "))
# b = int(input("Введите второе число: "))
# c = sqrt(a) - sqrt(b)
# print(c ** 2)

    ### Easy B ###
# from math import *
# a = int(input("Введите первое число: "))
# b = int(input("Введите второе число: "))
# c = tan(-(a * pi) / b)
# print(c)

    ### Medium A ###
# from random import randint
# from my_module_hw import sum_of_int
# num = randint(1000, 5000)
# print("Первоначальное число: ",num)
# print("Сумма цифр случайного числа: ",sum_of_int(num))

    ### Medium B ###
# from my_module_hw import *
# abs_n = int(input("Введите число для модуля: "))
# print("Число в модуле: ",num_abs(abs_n))

# sqrt_n = float(input("Введите число для извлечения корня: "))
# print(f"Корень числа {sqrt_n}: ", num_sqrt(sqrt_n))

# n = float(input("Введите число для возведения в степень: "))
# power_n = int(input("Введите степень: "))
# print(f"{power_n} - ая стпень {n}: ",num_pow(n, power_n))

    ### Hard A ###
# import random
# arr = list(map(int, input("Введите список: ").split()))
# max_num = max(arr)
# cnt = 0
# while True:
#     num = random.choice(arr)
#     cnt += 1
#     if num == max_num:
#         break
# print("Количество попыток: ", cnt)    


 ### Medium B ###
# from my_module_hw import my_ceil, my_sqrt, my_floor
# num = float(input())
# print(my_ceil(num))
# print(my_sqrt(num))
# print(my_floor(num))  