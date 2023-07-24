#x = print
#print(type(x))

    #знаки
    # = [присвоение]
    # == [равно]
    # >= [больше или равно]
    # <= [меньше ил равно]
    ### все 6 операций дают ответ через результат true или  false

#res = 5 >= 5
#print(res)

#res = "decode" > "apple"
#print(res)

### ord()    chr()
#print(ord('l'))   символ >>> код
#print(chr(99))     код >>> символ

    ### логические операторы ###
    # not   #превращает True в False и наоборот
    # in
    # or
    # and

#print(not 5 >= 9)

#print('c' in 'decode')
#print('k ' not in 'decode')

#number = 7
#print(number > 0  and  number % 2 == 0)

#number = 10
#print(number > 0 or 'n ' in 'apple')

#age = int(input("введите свой возраст: "))
#answer= input("есть карта: ")
#if answer == ("да"):
 #   has_card = True
#else:
#    has_card = False
#if age >= 21:
 #   print("Добро пожаловать!")
  #  if has_card:
   #     print("со входа на лево")
    #else:
   #     print("со входа на право ")
#elif age >= 18:
   # print("Входи, но не пей!")
#elif age >= 15:
 #   print("входи с окна")
#else:
 #   print("Проваливай!")

### Easy A ###
#name = input("Скажите ваше имя: ")
#if name == "Бонд":
#    print("добро пожаловать мистер Бонд")
#else:
#    print("добро пожаловать на борт")

### Easy B ###
#number  = int(input("введите число: "))
#if number % 2 == 0:
#    print("even")
#else:
#    print("odd")

### Easy C ###
#number_1 = float(input("введите первое число: "))
#number_2 = float(input("введите второе число: "))
#if  number_1 > number_2:
#    print("большее число: ",number_1)
#else:
#    print("Большее число: ",number_2)

### medium A ###
# number = int(input())
# if number // 100 == 0:
#    print("no")
# else:
#     print("yes")

### Medium B ###
# letter = input(("введите букву: "))
# if letter >= chr(97) and  letter <= chr(123):
#     print("small")
# elif letter >= chr(65) and letter <= chr(91):
#     print("big")
# else:
#     print("error")

### medium C ###
# import random
# a = random.randint(0,10)
# if a == 1:
#     print("one")
# if a == 2:
#     print("two")
# if a == 3:
#     print("three")
# if a == 4:
#     print("four")
# if a == 5:
#     print("five")
# if a == 6:
#     print("six")
# if a == 7:
#     print("seven")
# if a == 8:
#     print("eight")
# if a == 9:
#     print("nine")
# if a == 10:
#     print("ten")

### Hard A ###
# a = int(input("Введите первое число: "))
# b = int(input("Введите второе число: "))
# c = int(input("Введите третье число: "))
# d = int(input("Введите четвертое число: "))
# if (a > 0 and b > 0) and (c > 0 and d > 0):
#     print("oh no")
# else:
#     (a > 0 and b > 0) and (c < 0 or  d < 0)
#     print("it s ok")
# if (c > 0 and d  > 0) and (a > 0 and b > 0):
#     print("oh no")
# else:
#     (c > 0 and d > 0) and (a < 0 or  b < 0)
#     print("it s ok")

### hard B ###
# year = int(input("Введите год: "))
# if year % 400 == 0 and year % 100 == 0:
#     print("leap year")
# elif year % 100 == 0:
#     print("common")
# elif year % 4 == 0:
#     print("leap year")
# else:
#     print("common")
