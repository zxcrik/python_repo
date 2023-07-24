 ### max() min()  sum() ###
# dt = {
#     "OOP" : 98, 
#     "ICT" : 91,
#     "ADS" : 70
# }

# print(max(dt.values()))

# names = ["Olzhas", "Taman", "Qairant", "Yeskendir", "Alan", "Qanagat", "Zya"]
# print(max(names))
# print(max(names, key = len))     ###  В key , просто название функциии #

    ### sorted()    [].sort() ###      # sorted - для всех, автоматирует код / sort - для листа #
# st =  {"ads", "phys", "ict", "math", "oop"}
# list_st = list(st)
# list_st.sort()                <<<< sorted делает все действия сам / проще чем sort 
# print(list_st)

# print(sorted(st))

    ### Перевертыш ###
# names = ["Olzhas", "Taman", "Qairant", "Yeskendir", "Alan", "Qanagat", "Zya"]
# names.sort(key = len, reverse = True)               # ! Reverse изначально False ! #
# print(names)

    ### Easy A ###
# st = list(map(int, input("Введите числа: ").split()))
# su = sum(st)

# if su > 10:
#     print("More")
# if su < 10:
#     print("Less")
# if su == 10:
#     print("equal")

    ### Easy B ###
# name = input("Введите имя: ")
# zn = input("Введите зону: ")
# text = "https://www.{}.{}/"
# print(text.format(name, zn))

    ### Easy C ###
# tx = input("Введите текст: ")
# ls = set()

# for i in tx:
#     ls.add(i)
# print(len(ls))

    ### Easy D ###
# st = input("Введите строку: ").split()

# for i in st:
#     print(i,"-", len(i))

    ### Medium A ###
# lis = input("Введите список: ").split()
# print(lis[1::2])

    ### Medium B ###
# st = input("Введите сроку: ")
# is_alpha = True

# for i in range(len(st)):
#     if ord(st[i]) - i != 97:
#         is_alpha = False
#         break
#
# if is_alpha:
#     print("good")
# if is_alpha == False:
#     print("cringe")

    ### Medium C ###
# d = {
#     "Alan" : 12 

# }
# point = int(input("Оценка: "))

# if d["Alan"] < point:
#     d["Alan"] = point
# print(d)

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
#     for pair in f:*
#         print(pair[0], pair[1])
# else:
#     print("В списке нет пар элементов, дающих в сумме число {}".format(num))

    ### Hard B ###
# lis = list(map(int, input("Введите список чисел: ").split()))
# st = set(lis)
# print("Список без изменений: ", *lis)
# print("Список с изменениями: ", *st)

    ### Hard C ###
# sp = input("Введите список слов: ").split()
# dd = []
# rr = []

# for i in sp:
#     dd.append(i)
#     rr.append(len(i))

# di = dict(zip(dd,rr))
# for v in di.values():
#     if v > len(i):
#         dd.sort(reverse = True,key = len)
#         print(dd)
#         break
#     if v == len(i):
#         dd.sort()
#         print(dd)
#         break