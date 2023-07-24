    ### Функции ###
# def greeting(username, password):  # аргументы #
#     print(f"Hello, {username}! {password}")
# greeting("decode", 5)
# x = "python"
# greeting(x)    # не правильно #
# greeting(5.35)

### return ###
# 1) Данные возвращаются туда, где функция была вызвана #
# 2) Выход из функции #


# def sqrt(number):
#     res = number ** 0.5
#     return res

    # if res.is_integer():
    #     print(int(res))
    # else:
    #     print("{:.5f}".format(res))

# number = 10
# sqrt_number = sqrt(number)
# print(sqrt_number)

# def is_adult(age):
#     if age < 0:
#         return 
#     print("abc")
# is_adult(5)
# is_adult(-5)

# def my_max(a,b):
#     if a > b:
#         return a 
#     return b
# print(my_max(2,6))

# def my_max_2(a, b, *elements):
#     numbers = [a,b] + list(elements)
#     max_el = numbers[0]
#     for el in numbers:
#         if el > max_el:
#             max_el = el
#     return max_el
# print(max(2,5,8,6,3,17,7,8,5,78))
# print(my_max_2(2,5,8,6,3,17,7,8,5,78))

    # Локальные / глобальные переменные #
# age = 10        # Глобальная переменная / невозможно поменять внутри функции #
# def abc():
#     global age    # global дает возможность поменять глобальную переменную # 
#     age += 1
#     x = 5       # локальная переменная, используется только внутри функции #
#     print(age,x)
# abc()
# print(age)

    ### Аннотация типов ###  
# def sum_of_digits(num: int|float|bool) ->int :   # | - или(перечесление типов данных) / -> (подсказка получения типа данных после выполнения функции) #  
#     res = 0
#     while num > 0:
#         res += num % 10 
#         num //= 10
#     return res

# from lesson_14.home_work_14 import my_abc   # импорт другой функции #
# x = my_abc

# def is_prime(number: int) -> bool:
#     if number < 2:
#         return False
#     cnt = 0
#     for i in range(1, number + 1):
#         if number % i == 0:
#             cnt += 1
#     if cnt > 2:
#         return False
#     return True

    ### Easy A ###
# def hello():
#     print("Hi there, im using WhatsApp")
# hello()

    ### Easy B ###
# def show_age(age: int) -> str:
#     print(f"Im {age} years old")
# age = int(input("Введите возраст: "))
# show_age(age)

    ### Easy C ###
# def chek(num: int) -> bool:
#     if num % 2 != 0:
#         return False
#     return True
# num = int(input("Введите число: "))
# if chek(num) == True:
#     print("even")
# else:
#     print("odd")

    ### Easy D ###
# cnt = 0
# def sum_of_func(num: int) -> int:
#     for i in range(1,num + 1):
#         global cnt
#         cnt += i
#     return cnt
# num = int(input("Введите число: "))
# print(sum_of_func(num))

    ### Medium A ###
# def have_digit(st:str) -> str:
#         for i in st:
#                 if i.isdigit() == True:
#                     return ("Cool")
#         return ("hot")
# st = input("Введите строку: ")
# print(have_digit(st))

    ### Medium B ###
# def is_prime(num: int) -> bool:
#     if num < 2:
#         return False
#     cnt = 0
#     for i in range(1, num + 1):
#         if num % i == 0:
#             cnt += 1
#     if cnt > 2:
#         return False
#     return True
# num = int(input("Введите число: "))
# print(is_prime(num))

#     ### Medium C ###
# def sum_of_num(number: int) -> int:
#     suma = 0
#     while number > 0:
#         suma += number % 10        
#         number //= 10
#     return suma
# number = int(input("Введите число: "))
# print(sum_of_num(number))

    ### Hard A ###
# rt = []
# tp = []
# def ls(ms :int) -> int:
#     global rt, tp
#     for i in ms:
#         if i % 2 == 0:
#             rt.append(i)
#             rt.sort()
#         if i % 2 != 0:
#             tp.append(i)
#             tp.sort()
#     rt.extend(tp)
#     print(rt)
# ms = list(map(int, input("Введите список чисел: ").split()))
# ls(ms)

    ### Hard B ###
# def k_max(sp : int) -> int:
#     sp = set(sp)
#     sp = list(sp)
#     sp = sorted(sp,reverse = True)
#     print("Результат: ",sp[k - 1])
# sp = list(map(int, input("Введите список чисел: ").split()))
# k = int(input("Введите k - тый элемент: "))
# k_max(sp)

    ### Hard C ###
# def onlydigit(tx: str) -> str:
#     if tx.isnumeric() == True:
#         return ("very good")
#     if tx.isalpha() == True:
#         return ("so bad")
#     if tx.isalnum() == True:
#         return ("not bad")

# tx = input("Введите строку: ")
# print(onlydigit(tx))

