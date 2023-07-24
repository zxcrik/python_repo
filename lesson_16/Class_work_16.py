        ### Рекурсия ###
# def abc():
#     print("decode", end = " ")
#     abc()
# abc()

# def power(main: float| int, p: int):
#     if p == 0:
#         return 1
#     else:
#         return power(main, p - 1) * main
# print(power(2,4))

# i - опциональный параметр # 
# def one_to_number(num:int, i = 1,) -> None:         # !Опициональные параметры должны стоять после обязательных! #
#     print(f"num = {num}, i = {i}")
#     if i == num:           # Базовый случай #
#         return 
#     else:                              
#         one_to_number(num, i + 1)       # Рекурсивный случай #
# one_to_number(10)

# 0  1  1  2  3  5  8   13   21   34    55  89

# fibs = {}

# def fibonacci(n: int) -> int:
#     global fibs
#     if n in fibs:
#         return fibs[n] 

#     if n == 1:
#         return 0 
#     elif n == 2:
#         return 1 
#     else:
#         fibs[n-1] =  fibonacci(n - 1)
#         return fibs[n-1] + fibonacci(n-2)
    
# print(fibonacci(100))

    ### Easy A ###
# def rec():
#     print("This is recursion")
#     rec()
# rec()
    ### Easy B ###
# def nat_num(n:int,) -> None:
#     print(n, end = " ")
#     if n == 1:
#         return
#     else:
#         nat_num(n - 1)
# nat_num(12)

    ### Easy C ###
# def factorial(n: int) -> int:
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n - 1)
# print(factorial(5))

    ### Easy D ###
# def akker(m:int, n:int) -> int:
#     if m == 0:
#         return n + 1
#     if m > 0 and n == 0:
#         return akker(m - 1, 1)
#     if m > 0 and n > 0:
#         return akker(m - 1, akker(m,n - 1))
# print(akker(2,1))

    ### Medium A ###
# def sum_num(num:int, cnt = 0) -> int:
#     if num < 10:
#         return num
#     else:
#         return num % 10 + sum_num(num // 10)
# num = int(input("Введите число: "))
# print("Сумма чисел: ",sum_num(num))

    ### Medium B ###
# def sum_list(arr: list) -> int:
#     if len(arr) < 2:
#         return arr
#     else:
#         return sum(arr)
# arr = list(map(int, input("Введите список чисел: ").split()))
# print("Сумма чисел списка: ",sum_list(arr))

    ### Medium C ###
# def num_pow(num:int) -> str:
#     if num == 1:
#         return "yes"
#     elif num % 2 == 0:
#         return num_pow(num / 2)
#     else:
#         return "no"
# num = int(input("Введите число: "))
# print(num_pow(num))

    ### Hard A ###
