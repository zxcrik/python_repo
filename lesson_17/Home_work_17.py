    ### Easy A ###
# k = []
# v = []
# cnt = 0
# k_v = int(input("Введите количество пар, ключ - значение: "))      
# while cnt != k_v:                                                      # <- Ввод словаря с помощью консоли #
#     name_key = input("Введите имя ключа: ")
#     num_value = int(input("Введите значение ключа: "))
#     k.append(name_key)
#     v.append(num_value)
#     cnt += 1
#     d = dict(zip(k,v))
# print(d)
# try:
#     key = input("Введите ключ: ")
#     print("Значение ключа: ",d[f"{key}"])
# except KeyError:
#     print("This key does not exist!")

    ### Easy B ###
# num_1 = int(input("Введите первое число: "))
# num_2 = int(input("Введите второе число: "))
# print("Наименьшее значение: ",num_1 if num_1 < num_2 else num_2)

    ### Medium A ###
# arr = list(map(int, input("Введите список: ").split()))
# for i in arr:
#     if i % 3 == 0 and i % 5 == 0:
#         raise Exception("Такое число присутствует")
#     else:
#         raise Exception("Такое число отсутствует")

    ### Medium B ###
# try:
#     a = int(input("Введите первое число: "))
#     b = int(input("Введите второе число: "))
#     c = int(input("Введите произведение чисел ab: "))
# except ValueError:
#     print("Вводите только целые числа !")
# else:
#     if a * b == c:
#         raise Exception(True)
#     else:
#         raise Exception(False)

    ### Hard A ###
# try:
    # cnt = 0
    # num_1 = float(input("Введите первое число: "))
    # num_2 = float(input("Введите второе число: "))
    # print(operations := ('+' , '-', '*', '/', '**' , '//', '%'))
    # ope = input("Введите операцию: ")
    # if ope == "+":
    #     print("Результат: ",num_1 + num_2)
    #     cnt += 1
    # if ope == "-":
    #     print("Результат: ", num_1 - num_2)
    #     cnt += 1
    # if ope == "*":
    #     print("Результат: ", num_1 * num_2)
    #     cnt += 1                                   # <- cnt это счетчик операций, без cnt всегда выводится print о том что операция не найдена #
    # if ope == "/":
    #     print("Результат: ", num_1 / num_2)
    #     cnt += 1
    # if ope == "**":
    #     print("Результат: ", num_1 ** num_2)
    #     cnt += 1
    # if ope == "//":
    #     print("Результат: ", num_1 // num_2)
    #     cnt += 1
    # if ope == "%":
    #     print("Результат: ", num_1 % num_2)
    #     cnt += 1
    # if cnt == 0:
    #     print(f"Операции {ope} не обнаружено")
# except ValueError:
#     print("Ошибка: Был введен не соответствующий тип данных")
# except ZeroDivisionError:
#     print("Ошибка: Деление на ноль")

    ### Hard B ###
# def num_div(number: int) -> bool:
#     if number < 3:
#         print("Введите число больше")
#     else:
#         for i in str(number):
#             if int(i) % 3 == 0:
#                 return True
#         return False
# number = int(input("Введите число для проверки: "))
# print(result := True if num_div(number) else False)