### frozenset() ###
# st1 = frozenset({1,2,3})
# print(st1)

### tuple() ###
# numbers = (1,2,3,4)          # Только count и index #
# print(numbers[-1])
# print(numbers[:2])
# print(numbers) 

# if 2 in numbers:
#     print("YES")
# if 5 in numbers:
#     print("YES THO")
# if 7 not in numbers:
#     print("NOT")

# t = ("decode", )    # Создание tuple() #
# print(type(t))

    ### dict() ###
# x1 = {}       # Пустой dict() #
# x2 = {"python" , "c++"}       # Заполненый set

# x3 = {"abc": 1,       #  Заполненый dict #     # Ключ - значение #
#       5: 2,            # Одна пара или one item #   
#       0.2: 3
# }                       # Указывать разные ключи #
# print(type(x3))
# print(len(x3))

    ### Как использовать ключи ? ###
# print(x3[0.2])

# student = {
#     "name" : "Erlan",
#     "age" : 27 ,
#     "height" : 1.75,
#     "GPA" : 4.0 ,
#     "subjects" : ["ADS", "ICT", "OOP"],
#     "points" : [70, 75, 96]
# }
# print(student["subjects"][-1])
# print(sum(student["points"]) / len(student["points"]))

# x = {
#     "abc" : 100,
#     "def" : "decode"
# }
# x["def"] = "python"      # Обновляется значение #
# x["qwerty"] = "с++"   # создается с указанным значением #
# del x["abc"]            # Удалить значение #

# print(x)

    ### Методы ###
### .get() ###
# student = {
#     "name" : "Erlan",
#     "age" : 27 ,
#     "height" : 1.75,
# }
# print(student["name"])          # Получаем ошибкув случае отсутствии элемента #
# print(student.get(["name"]))     # Выводит none #

### .pop() ###
# deleted_value = student.pop("height")
# print(student)

### .popitem() ###
# d = student.popitem()    # возвращается как tuple #
# print(student)
# print(d)

### .update() ###
# a = {
#     1 : 1,
#     2 : 4
# }

# b = {
#     3 : 9,
#     4 : 16
# }
# a.update(b)       # добавление одного dict в другой #
# a.update({5:25})
# print(a)

### .dict.fromkeys() ###                        # Возвращение нового словаря #
# letters = ["a","b","a","c","a","b", "d","c"]

# d = dict.fromkeys(letters,0)
# print(d)

# for letter in letters:
#     d[letter] += 1        
# print(d)

### .keys() ###
# student = {
#     "name" : "Erlan",
#     "age" : 27 ,
#     "height" : 1.75,
# }

# print(student.keys())    # дает все ключи #

# for el in student.keys():
#     print(el)

### .values() ###
# print(student.values())   # дает все значения ключей #

### .items() ###
# print(student.items())              # Массив значений #
                                    
# for k , v in student.items():         
#     print()        # пробежка по ключам и значениям #

### zip() ###

# x = ["Python", "c++", "js", "java"]
# y = [3.10, 14.8, 6,8]

# d = dict(zip(x,y))      # Кто стоит первый - ключи , второй - значение #
# print(d)

    ### Easy A ###
# keys = ["Ten", "Twenty", "Thirty"] 
# values = [10, 20, 30] 
# print(di := dict(zip(keys,values)))

    ### Easy B ###
# sample_dict = { 
#     "class": { 
#         "student": { 
#             "name": "Mike", 
#             "marks": { 
#                 "physics": 70, 
#                 "history": 80 
#             } 
#         } 
#     } 
# } 
# print(sample_dict.values())
# print(sample_dict["class"]["student"]["marks"]["history"])

    ### Easy C ###
# d = { 
#     "math": 75, 
#     "physics": 90, 
#     "ict": 64, 
#     "ads": 70 
# }
# min_v = min(d.values())

# for k , v in d.items():
#     if v == min_v:
#         print(k)

    ### Easy D ###
# info = {
#     "name": "Aidana",
#     "grades": [96, 78, 67, 73, 90]
# }

# x = info["grades"]
# print(sum(x) / len(x))

    ### Medium A ###
# sn = int(input("Введите кол-во учеников: "))
# cnt = 0
# nm = []
# grad = []

# while cnt != sn:
#     name = input("Введите имя: ")
#     gr = int(input("Введите оценку студента: "))
#     nm.append(name)
#     grad.append(gr)
#     cnt += 1
# d = dict(zip(nm,grad))
# print(d)

    ### Medium B ###
# st = input("Введите строку: ").split()
# d = dict.fromkeys(st,0)

# for word in st:
#     d[word] += 1
# print(d)

    ### Medium C ###
# sp = input("Введите список чисел: ")
# d = dict.fromkeys(sp,0)

# for word in sp:
#     d[word] += 1

# x1 = dict(sorted(d.items()))
# print(x1)

    ### Hard A ###                  
