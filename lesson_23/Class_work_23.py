    ### Классы ###
### наследование ###
# class Pavozka:
#     cnt_of_wheels = 4

# class Car(Pavozka):                            # родительский класс #
#     def turn_on(self):
#         print("Машина заведена!")

# class ElectroCar(Car):              # класс наследник | дочерний класс #
#     battery_level = 90

#     def turn_on(self):
#         super().turn_on()         # обращение к родительскому методу #
#         print(f"Электро - Машина заведена! Зарядка {self.battery_level} кВт")

# tesla = ElectroCar()
# tesla.turn_on()
# print(tesla.cnt_of_wheels)

# class Human:
    # def __init__(self, name, surname, age):
    #     self.name = name
    #     self.surname = surname
    #     self.age = age

# class Student(Human):
#     def __init__(self, name, surname, age, course, gpa):
#         super().__init__(name, surname, age)
#         self.course = course
#         self.gpa = gpa
    # def show_info(self):
    #     print(self.name, self.surname, self.age, self.course, self.gpa)

# std1 = Student("Erlan", "Amanov",18, 1, 3.33)
# std2 = Student("Timur", "K",14, 8, 4)
# std3 = Student("Erlan", "Amanov",18, 1, 3.33)

# for student in [std1, std2]:                # пробежка по всем данным с помощью функции #
#     student.show_info()

    ### псевдо код / полиморфизм ###
# class Temp:
#     def __init__(self, value: int|float, scala: str):
#         self.value = value
#         self.scala = scala

#     def __init__(self, value: int|float):
#         self.value = value
#         self.scala = "C"
    
#     def __init__(self, scala: str):
#         self.value = 0
#         self.scala = scala

#     def __init__(self):
#         self.value = 0
#         self.scala = "C"

# t1 = Temp("K") # 0k
# t2 = Temp() # 0c
# t3 = Temp(36.6) # 36.6c

    ### Инкапсуляция / приватизация ###
# class Human:
#     def __init__(self, name, surname, age):
#         self.name = name
#         self.surname = surname
#         self.__age = age                # приватизация #

#     def show_info(self):
#         print(self.name, self.surname, self.__age)
    
#     def get_age(self) -> int:
#         return self.__age
    
# h1 = Human("Vanya", "Petrov", 12)
# h1.show_info()

# print(h1.get_age())

    ### Easy С ###
# class Country:
#     def __init__(self, population: dict = {}):
#         self.population = population
#     def get_population(self):
#         for v in self.population.values():
#             print(f"{v} - человек")
#     def set_population(self):
#         for k in self.population.keys():
#             print(f"{k}")

# class Russia(Country):
#     def __init__(self, population):
#         super().__init__(population)

# class Canada(Country):
#     def __init__(self, population):
#         super().__init__(population)

# class Germany(Country):
#     def __init__(self, population):
#         super().__init__(population)

# ru = Russia({

# })
# ru.get_population()
# ru.set_population()

# cn = Canada({

# })
# cn.get_population()
# cn.set_population()

# gm = Canada({

# })
# gm.get_population()
# gm.set_population()

    ### Easy A ###
# class Games:
#     def __init__(self, name, year):
#         self.name = name
#         Games.year = year
#     def get_name(self):
#         return self.name

# class PCGames(Games):
#     def __init__(self, name, year, developer):
#         super().__init__(name, year)
#         self.developer = developer

#     def getName(self):
#         return f"{self.name} by {self.developer} (PC)"


# class PS4Games(Games):
#     def __init__(self, name, year, publisher):
#         super().__init__(name, year)
#         self.publisher = publisher

#     def getName(self):
#         return f"{self.name} published by {self.publisher} (PS4)"


# class XboxGames(Games):
#     def __init__(self, name, year, genre):
#         super().__init__(name, year)
#         self.genre = genre

#     def getName(self):
#         return f"{self.name} ({self.genre}) (Xbox)"


# class MobileGames(Games):
#     def __init__(self, name, year, platform):
#         super().__init__(name, year)
#         self.platform = platform

#     def getName(self):
#         return f"{self.name} ({self.platform}) (Mobile)"

    ### Medium A ###
# class Human:
#     def __init__(self, name, age, country):
#         self.name = name
#         self.age = age
#         self.country = country

# class Student(Human):
#     def __init__(self, name, age, country, univercity_name, gpa):
#         super().__init__(name, age, country)
#         self.univercity_name = univercity_name
#         self.gpa = gpa
#     def show_info(self):
#         print(self.name, self.age, self.country ,self.univercity_name, self.gpa)

# std = Student()
# std.show_info()

    ### Medium B ###
# class Shape:
#     def __init__(self,a1):
#         self.a1 = a1
#     def get_area(self):
#         return self.a1 * self.a1

# class Triangle(Shape):
#     def __init__(self, a, b = 0, c = 0):
#         self.a = a
#         self.b = b
#         self.c = c
#     def get_area(self):
#         return (self.a * self.b * self.c) / 2
    
# class Square(Shape):
#     def __init__(self,a):
#         super().__init__(a)

# sq = Square(4)
# tr = Triangle(4)
# print(tr.get_area())
# print(sq.get_area())


