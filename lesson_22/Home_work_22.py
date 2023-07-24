    ### Easy ###
# class Almir:
#     def __init__(self, name: str, age: int):
#         self.name = name
#         self.age = age
#     def check_al(self):
#         if self.name.title() != "Альмира":
#             return f"Я не {self.name}, а Альмира"
#         else:
#             return "Альмира"
# nm = input("Введите имя: ")
# ag = int(input("Введите возраст: "))
# p1 = Almir(nm, ag)
# print(p1.check_al())

    ### Medium ###
# class Gazirovka:
#     def __init__(bf, ch_additive: str|int):               # bf вместо self, т.к можно писать любую ссылку #
#         bf.ch_additive = ch_additive
#     def show_my_drink(bf):
#         print("В газировке есть цифры?\nда|yes\nнет|no")
#         answ = input("Введите ответ: ")
#         if answ == "да" or answ == "yes":
#             try:
#                 num_gaz = int(input("Введите номер на газировке: "))
#             except ValueError:
#                 return("Не правильный тип данных!\nПопробуйте еще раз")
#             else:
#                 return("Обычная газировка")
#         if answ == "нет" or answ == "no":
#             try:
#                 tas_gaz = input("Введите добавку газировки: ")
#             except ValueError:
#                 return("Не правильный тип данных!\nПопробуйте еще раз")
#             else:
#                 return(f"Газировка и {tas_gaz}")
# gazi = Gazirovka(input("Введите газировку: "))
# print(gazi.show_my_drink())

    ### Hard ###
# class Triangle:
#     def __init__(self,num1: int|float, num2: int|float, num3: int|float):
#         self.num1 = num1
#         self.num2 = num2
#         self.num3 = num3
#     def is_it_triangle(self):
#         if self.num1 < 0 or self.num2 < 0 or self.num3 < 0:
#             return "С отрицательными числами ничего не выйдет!"
#         elif (self.num1 - self.num2) > 10 or (self.num2 - self.num1) > 10 or (self.num2 - self.num3) > 10 or (self.num3 - self.num2) > 10 or (self.num1 - self.num3) > 10 or (self.num3 - self.num1) > 10:
#             return "Жаль, но из этого треугольник не сделать."
#         else:
#             return "Ура, можно построить треугольник!"
# try:
#     num_1 = int(input("Введите первое число: "))
#     num_2 = int(input("Введите второе число: "))
#     num_3 = int(input("Введите третье число: "))
# except ValueError:
#     print("Нужно вводить только числа!")
# else:
#     build_tr = Triangle(num_1, num_2, num_3)
#     print(build_tr.is_it_triangle())