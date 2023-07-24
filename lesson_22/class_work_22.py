    ### class/классы ###
# class Human:
#     name = "Erlan"     # аттрибут name #
#     age = 24           # аттрибут age #

# human1 = Human()
# human2 = Human()

# print(human1.name)
# print(human1.age)
# print(human2.name)
# print(human2.age)

    ### Пример 2 ###
# class Human:
    # self - универсальный объект #
    # self - ссылка на саму себя #
#     def __init__(self, name: str, age: int,):         ## конструктор ##
#         self.name = name                             ## аттрибут name ##
#         self.age = age                               ## аттрибут age ##
#         self.salary = 0
#         self.cars = ["toyota", "bmw"]
#     def grading(self, salary_update: int|float):         # метод grading #
#         self.salary += salary_update
#     def bd(self):
#         self.age += 1 


# human1 = Human("Erlan", 24)
# human2 = Human("Abay", 15)
# print(human1.salary)
# human1.grading(200_000)
# print(human1.salary)

# print(human1.name)           # обращение к аттрибутам #
# print(human1.age)   
# print(human2.name)
# print(human2.age)
# print(human2.weight)

    ### метод isinstance() ###
# n = 5
# if type(n) == int:
#     print("да")
# if isinstance(n,int):
#     print("да")

# print(type(human2) == Human)
# print(isinstance(human2, Human))

    ### импортирование классов ###
# from class_work_22 import Human
# h = Human("Abay", 15)
# h.bd()
# print(h.name)
# print(h.age)

    ### Easy A/B/C ###
# from math import *
# class point:
#     def __init__(self, x: int, y: int):
#         self.x = x
#         self.y = y
#     def dist(self, other_point):
#         return sqrt((other_point.x - self.x)**2 + (other_point.y - self.y)**2)

# x1 = int(input("Введите число x1: "))
# y1 = int(input("Введите число y1: "))
# p1 = point(x1,y1)

# x2 = int(input("Введите число x2: "))
# y2 = int(input("Введите число y2: "))
# p2 = point(x2,y2)

# print(p1.dist(p2))
# x = int(input("Введите число x: "))
# y = int(input("Введите число y: "))
# p = point(x,y)
# n = input("Введите букву: ")
# if n == "x":
#     print(p.x)
# if n == "y":
#     print(p.y)

    ### Medium ###
# from math import sqrt
# class Rect:
#     def __init__(self,num1: int, num2: int):
#         self.num1 = num1
#         self.num2 = num2
#     def is_square(self):
#         if self.num1 == self.num2:
#             return True
#         else:
#             return False
#     def get_perimetr(self):
#         return (self.num1 + self.num2) * 2
#     def get_area(self):
#         return self.num1 * self.num2
#     def get_diagonal(self):
#         d = sqrt(self.num1 ** 2 + self.num2 ** 2)
#         return d
# x = int(input("Введите первую сторону: "))
# y = int(input("Введите вторую строну: "))
# res = Rect(x,y)
# print(res.get_perimetr())
# print(res.get_area())
# print(res.get_diagonal())

    ### Hard ###
# class Shop:
#     def __init__(self,products: dict = {}):
#         self.products = products
#         self.basket = {}
#     def add_to_basket(self, product_name: str):
#         if product_name not in self.products.keys():
#             print(f"Товара {product_name} у нас нет!\n")
#             return
#         if product_name in self.basket.keys():
#             self.basket[product_name] += 1
#         else:
#             self.basket[product_name] = 1
#         print(f"товар {product_name} был добавлен в корзину!\n")

#     def remove_from_basket(self, product_name: str) -> None:
#         if product_name in self.basket.keys():
#             if self.basket[product_name] > 0:
#                 self.basket[product_name] -= 1
#                 print(f"Товар {product_name} был убран из корзины!\n")
#         else:
#             print(f"Товара {product_name} нет в корзине!\n")
#     def total_price(self):
#         total = 0
#         for prd_name, prd_cnt in self.basket.items():
#             total += prd_cnt * self.products[prd_name]
#         return total
#     def avg_price(self):
#         return self.total_price
# shop = Shop({
#     "bread" : 150,
#     "milk" : 200,
#     "juice" : 300,
#     "fruits" : 250
# })
# shop.add_to_basket("bread")
# shop.add_to_basket("bread")
# shop.add_to_basket("bread")

# shop.add_to_basket("fruit")
# shop.add_to_basket("fruit")

# shop.remove_from_basket("fruit")