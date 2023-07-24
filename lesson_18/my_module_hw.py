    ### Medium A ###
# def sum_of_int(num: int) -> int:
#     return sum(map(int, str(num)))

    ### Medium B ###
# from math import * 
# def num_abs(num: int) -> int:
#     if num > 0:
#         return num
#     if num < 0:
#         return num * (-1)

# def num_sqrt(num: float) -> int:
#     return sqrt(num)


# def num_pow(num: float, power: int) -> int:
#     cnt = 0
#     n = num
#     while cnt != (power - 1):
#         num *= n
#         cnt += 1
#     return num

    ### Medium B ###
# def my_sqrt(num: int|float) -> float:
#     return num ** 0.5

# def my_ceil(num: int|float) -> int:                         # округление вверх #
#     if num == int(num):
#         return int(num)
#     return int(num + 1)        

# def my_floor(num: int|float) -> int:                   # округление вниз # 
#     return int(num)