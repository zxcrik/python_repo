    ### Easy A ###
# def number_unreverse(num: int, res = 0) -> int:
#     if num == 0:
#         return res
#     else:
#         res = res*10 + num % 10
#         return number_unreverse(num // 10, res)
# num = int(input("Введите число: "))
# print(number_unreverse(num))

    ### Medium A ###
# def power(x: float| int, y: int) -> int:
#     if y <= 0:
#         return 1
#     else:
#         return power(x, y - 1) * x
# x = int(input("Введите число для возведения в степень: "))
# y = int(input("Введите степень: "))
# print("Результат: ",power(x,y))

    ### Hard A ###
# def monoton_seq(size: int, i = 1, cnt = 0) -> None:
#     if size == 0:
#         return
#     if cnt < i:
#         print(i, end = " ")
#         monoton_seq(size - 1, i, cnt + 1)
#     elif cnt == 1:
#         monoton_seq(size, i + 1, cnt = 0)

# size = int(input("Размер: "))
# monoton_seq(size)