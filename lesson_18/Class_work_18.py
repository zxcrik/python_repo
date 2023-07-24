    ### Модули ###
# 1 # 
# import math  # импортируем сам модуль 
# num = math.sqrt(10)
# num2 = math.pi
# num3 = math.sin(num)
# print(num, num2,num3)]

# 2 #
# from math import sqrt, pi, sin           # Возможность пользоваться тремя импортированными #
# num = sqrt(10)
# num2 = pi
# num3 = sin(num)
# print(num, num2, num3)

# 3 #
# from math import *
# print(sin(12))
# print(pi)
# print(hypot(6,8))

# num = 5.3
# print(ceil(num))        # округление вверх #
# print(floor(num))       # Округление вниз #
 
# from bs4 import BeautifulSoup as bs 
                                             # сокращение  as - как #
# import math as m 

# from random import randint as rint, randrange as rrange
# from random import choices
# names = ["Alan", "Erlan", "Ernar", "Qairat"]
# print(choices(names))


# import my_module as mm
# print(mm.factorial(5))
# print(mm.student["age"])
# print(mm.__name__)

# import sys                     ### Импорт системы ###
# sys.path.append("..")         ### Выход в другие файлы ###
# from lesson_15.class_work_15 import sum_of_num

# sys.path.append("../../..")    <- выход из 3 папок назад

    ### Easy A ###
# import my_module as mm 
# print(mm.var[0])

    ### Easy B ###
# import my_module as mm
# print(mm.student["name"], mm.student["age"])

    ### Easy C ###
# from random import randint
# a = int(input("Введите первое число: "))
# b = int(input("Введите второе число: "))
# print("Случайное число: ",c := randint(a,b))

    ### Medium A ###
# import my_module as mm
# word = input("Введите слово: ")
# print(mm.rev_word(word))

    ### Medium B ###
# from math import sin, sqrt, pow
# x = int(input("Введите x: "))
# y = int(input("Введите y: "))
# a = sqrt(sin(x) + y ** 3) + sqrt(x + y)
# b = (x + x) + y
# print("Результат: ", c := a / b)

    ### Medium C ###
# from math import sin, cos, pow, exp
# a = sin(5) + pow(1.75, 2)
# b = 3 * (exp(1) * cos(7))
# print("Результат: ",c := a / b)