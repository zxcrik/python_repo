    ### Try ---  Excepct ###
# while True:
#     try:
#         age = int(input("Введите возраст: "))
#         break
#     except:
#         print("Введите нормально!")
#     else:                                      # else - можно использовать вместо break#
#         print("Все успешно!")


# print("Все ок!")

# try:
#     ls = []
#     size = int(input("Размер: "))

#     for i in range(size):
#         el = input()
#         ls.append(el)
#     print(ls[3])

# except TypeError:
#     print("Размер ввели не так!")
# except IndexError:
#     print("Индекс вышел за рамки!")
# except NameError:
#     print("Использеутся переменная которой нет! ")
# except:                                               # Пустой except выводит любые другие не указанные ошибки #
#     print("Некая неизвестная ошибка!")

# try:                                    # Помещаем код с возможной ошибкой #
#     a = int(input("Введите число: "))
# except:                               # Что делать если код сломался # 
#     print("Введите целое число: ")
# else:                               # Что делать если код успешно сработал #
#     print(f"Ваш возраст {a}")
# finally:                            # Сработает в любом исходе #
#     print("Конец")

    ### raise ###
# def number_unreverse(num: int, res = 0) -> int:
#     if type(num) != int:
#         raise TypeError("Функция должна принимать только int")
    
#     if num == 0:
#         return res
#     else:
#         res = res*10 + num % 10
#         return number_unreverse(num // 10, res)
# num = int(input("Введите число: "))
# print(number_unreverse(num))

    ### Тернарный оператор ###
# num = int(input("Число: "))

# if num % 2 == 0:
#     print("Четное")
# else:
#     print("не четное")

# print("Четное" if num % 2 == 0 else "Нечетное")

# res = "Положительное" if num > 0 else "нейтральное или отрицательное"
# print(res)

# def my_abs(number: int) -> int:
    # if number >= 0:
    #     return number
    # else:
    #     return number * (-1)
    # return number if number >= 0 else number * (-1)         # Вариант покороче #

# n = int(input("Введите число: "))
# res = "positive" if n > 0 else "negative" if n < 0 else "neitral"

    ### Easy A ###
# num = int(input("Введите число: "))
# if num < 0:
#     raise ValueError("Ошибка ввода!")
# else:
#     print("its ok")

    ### Easy B ###
# try:
#     number = int(input("Введите число: "))
#     if type(number) == int:
#         print(number)
# except ValueError:
#     print("srsly?")

    ### Easy C ###
# text = input("Введите строку: ")
# if text != text.capitalize():
#     raise NameError("Чел ты...")
# else:
#     print(text)


# two_numbers = list(map(int, input().split()))
# try:
#     a, b = two_numbers  # Может сломаться
# except:
#     a = two_numbers[0]
#     b = int(input("Введите второе число: "))
# print(f"{a} + {b} = {a+b}")


# numbers = list(map(int, input("Введите список: ").split()))
# for i in range(len(numbers) - 1):
#         try:
#             print(f"{numbers[i]} / {numbers[i + 1]} = {numbers[i] / numbers[i + 1]}")
#         except:
#             print(f"Невозможно вычислить {numbers[i]} / {numbers[i + 1]}")

    ### Medium A ###
# name = input("Введите имя: ")
# if name.isalpha() != True:
#     raise NameError("Чел ты...")
# else:
#     print("welcome")

    ### Medium B ###
# mail = input("Введите почту: ")
# if mail.count('@') >= 2 or mail.count('@') < 1:
#     raise NameError("Чел ты...")
# else:
#     print("ok")

    ### Medium C ###
# mail = input("Введите почту: ")
# if mail.islower() != True or mail.isalpha() != True:
#     raise NameError("Чел ты...")
# else:
#     print("ok")