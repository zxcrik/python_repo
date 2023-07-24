    ### Easy A ###
# def sqr(a,n: int) -> float:
#     return pow(a,n)
# a = int(input("Введите число: "))
# n = int(input("Введите степень: "))
# print("Результат:",sqr(a,n))

    ### Easy B ###
# def is_year_leap(year: int) -> bool:
#     if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
#         return True
#     return False
# year = int(input("Введите год: "))
# print("Результат: ", is_year_leap(year))

    ### Medium A ###
# def nod(a,b: int) -> int:
#     while b != 0:
#         a, b = b, a % b
#     return a
# a = int(input("Введите 1 - ое число: ")) # НОД 36 и 40 == 4, но не 8 #
# b = int(input("Введите 2 - ое число: "))
# print("НОД: ",nod(a,b))        

# 2 способ решения #
# import math
# a = int(input("Введите 1 - ое число: ")) 
# b = int(input("Введите 2 - ое число: "))
# print("НОД: ",math.gcd(a,b))

    ### Medium B ###
# def sa(ls: int) -> float:
#     return sum(ls) / len(ls)
# ls = list(map(int, input("Введите список чисел через пробел: ").split()))
# print("Среднее арифметическое:",sa(ls))       # Среднее арифметическое [3,2,6,0] == 2.75, но не 5.5 #

#     ### Hard A ###
# def sum_num(ls: int) -> int:
#     return sum(int(digit) for digit in str(ls))

# def sort_arr(arr: list) -> list:
#     return sorted(arr, key = sum_num)

# arr = list(map(int, input("Введите список чисел: ").split()))
# print("Исходный массив:", arr)
# print("Отсортированный массив:", sort_arr(arr))
# print("Сумма цифр отсортированного массива: ",sums_of_digits := [sum_num(ls) for ls in sort_arr(arr)])

    ### Hard B ###
# def rev(st: str) -> str:
#     return st[::-1]
# st = input("Введите строку: ").split()
# print(*rev(st))
