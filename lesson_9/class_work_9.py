    ### Массивы ###
# empty = []  -- Пустой массив

# names  = ["Alan", "Erlan","Qairat","dima", "Abay"]
# print(names)

    ### Индексы ###
# print(names[1]  , names[3])

    ### Длина ###
 ### Функция - len ###  Length
# print(len(names))

    ### Операции над массивами ###
# (+)  (*) 
# students = ["Alan", "Erlan"]
# proffessors = ["Abay", "Qairat"]
# print(students + proffessors )

# print(students * 3)   res: ["Alan", "Erlan", "Alan", "Erlan", "Alan", "Erlan"]

    ### Генерация списка ###
# ls = [0] * 3
# print(ls)

    ### Изменение значения элемента ###
# names  = ["Alan", "Erlan","Qairat","dima", "Abay"]
# names[0] = "Amir"

    ### swap ###      swap - поменять 
# name = "Saudabekov"
# surname = "Alan"
# name , surname = surname , name 

# names[0] , names[-1] = names[-1], names[0]

    ### Срезы ###
# names = ["Alan", "Erlan","Qairat","dima", "Abay","Akhan", "Amir"]
# print(names[1:7:2])

#    0     0      0
# [Start, stop, step]
# 0 (с конца ) : до конца : +1

# print(names[::-1])  # reversing

# a = [0] * int(input("Введите размерность: "))
# for i in range(len(a)):
#     a[i] = int(input("Введите число: "))
# print(a[i])


    ### Итерация/пробежка ###
# numbers = [2, 6, -9, 4, 0, -7, -12, 1]
# cnt = 0

# for el in numbers:    ### 1 вариант итерации ###
#     if el < 0:
#         cnt += 1

# for i in range(len(numbers)):    ### 2 варинт итерации ###
#     if numbers[i] < 0:              ### Если нужно использовать индексы массива ###
#         cnt += 1
# print(cnt)

    ### Функция map() ###
# numbers = [5, 9, 123.456, False, "789"]
# print(list(map(int,numbers)))

    ### Как принимать с консоли split() ###
# numbers = list(map(int,input().split()))    # Другой тип данных #
# print(numbers)
    ### Методы списка ###
    ### .clear() ###
# x = [1,2,3]
# x.clear()
# print(x)

    ### .copy() ###
# busket = ["phone", "mackbook", "bread"]
# history = busket.copy()

# busket.clear()
# print(history)

    ### .count() ###
# numbers = [0,34,67,3,8,0,89,5]
# print(numbers.count(0))

    ### .index() ###
# names = ["Alan", "Erlan","Qairat"]
# print(names.index("Qairat"))

    ### .insert() ###
# names = ["Alan", "Erlan","Qairat", "Abay"]
# names.insert(2,"Dima")
# print(names)

    ### .extend() ###
# x = ["a", "c","b"]
# y = ["y", "j","i"]
# y.extend(x)
# print(y)

    ### .pop() ###
# names = ["Alan", "Erlan","Qairat", "Abay"]
# del_el = names.pop(2)
# print(names)
# print(del_el)

    ### .remove() ###
# names.remove("Abay")
# print(names)

    ### .sort() ###
# names = ["Nurai", "Erlan","Ziya", "Abay", "Qairat"]
# names.sort()
# print(names)

    ### .reverse() ###
# names = ["Nurai", "Erlan","Ziya", "Abay", "Qairat"]
# names.reverse()
# print(names)

    ### in ###
# names = ["Alan", "Erlan","Qairat","Abay","Qairat","Qairat",]
# while "Qairat" in names:
#     names.remove("Qairat")
# print(names)

    ### Умножение ###
# numbers = [1,7,4,5,8]
# from math import prod
# print(prod(numbers))

    ### Распаковка ###
names = ["Nurai", "Erlan","Ziya"]
print(*names)

    ### Easy A ###
# num = int(input("Введите кол-во элементов: "))
# a = []
# for i in range(num):
#     stroke = input("Введите строку: ")
#     a.append(stroke)
# print(a)
    
    ### Easy B ###
# print(numbers := list(map(int,input("Введите числа: ").split()))) 

    ### Easy C ###
# numbers = list(map(int,input("Введите числа: ").split())) 
# if len(numbers) == 1:
#     print(numbers[0])
# else:
#     print(numbers[0], numbers[-1])

    ### Easy D ###
# sunumbers = list(map(int,input("Введите числа: ").split())) 
# print("Сумма =",sum(sunumbers))

    ### Medium A ###
# number = list(map(int,input("Введите числа: ").split())) 
# for el in range(len(number)):
#     if number[el] > 0:
#         print(number[el])

    ### Medium B ###
# li = list(map(int, input("Введите числа: ").split()))
# li.sort(reverse = True)
# print(*li)

    ### Medium C ###
# sp = list(map(int, input("Введите числа: ").split()))
# print("Максимальное число: ",max(sp))

    ### Hard A ###
# numbers = list(map(int, input("Введите список: ").split()))
# num = int(input("Введите число: "))
# f = []

# for el in range(len(numbers)):
#     for j in range(el + 1, len(numbers)):
#         if numbers[el] + numbers[j] == num:
#             f.append((numbers[el], numbers[j]))
# if f:
#     print("Найдены следующие пары элементов, дающие в сумме число {}: ".format(num))
#     for pair in f:
#         print(pair[0], pair[1])
# else:
#     print("В списке нет пар элементов, дающих в сумме число {}".format(num))

#     ### Hard B ###
# li = list(map(int,input("Введите список: ").split()))
# print(set(li))

    ### Hard C ###
# hp = []
# num = int(input("Введите кол-во слов: "))
# for i in range(num):
#     wr = input("Введите слово: ")
#     hp.append(wr)

