###  итерация - пробежка ###
# text = "DeCode"
# for letter in text:
#     print(letter)

# repeat = 10
# for i in range(repeat):
    # print(i)

# for i in range(0,101,2):
#     print(i)

# for i in range(100,49,-10):
#     print(i)

# range(7)  0, 1, 2, 3, 4, 5, 6
# range(2,7) 0, 1, 2, 3, 4, 5, 6 
# range(2,7,2) 2, 4, 6 

# range(start,stop,step) SSS

# ## sep=" " ### нужно когда много переменных / промежуток
# print("hello",123, "world", True, sep="")

### end ###
# print("hello", end = "!")
# print(123)
# print("world")
# a = "world"
# b = 123
# c = "qwerty"
# print(a,b,c, sep="," , end=".")

    ### Easy A ###
# for i in range(5,16):
#     if i != 10:
#         print(i, end=" ")
    ### Easy B ###
# n = int(input("Введите число: "))
# for i in range(1,n+1):
#     print(i)

    ### Easy C ###
# l = int(input("Введите первое число: "))
# r = int(input("Введите второе число: "))
# if l % 2 == 1:
#     l += 1
# for i in range(l,r+1,2):
#     print(i, end=" ")

    ### Easy D ###
# l = int(input("Введите первое число: "))
# r = int(input("Введите второе число: "))
# if l % 2 == 0:
#     l -= 1
# for i in range(l,r-1,-2):
#     print(i, end=" ")

    ### Medium A ###
# string = input("Введите строку: ")
# for i in (string):
#     print(i, sep=" ", end=" ")

    ### Medium B ###
# a = int(input("Введите первое число: "))
# b = int(input("Введите первое число: "))
# sum = 0
# for i in range(a, b+1):
#     sum += i
# print(sum, end=" ")

    ### Medium C ###
# import math
# a = int(input("Введите первое число: "))
# b = int(input("Введите второе число: "))
# nok = 0
# d = math.gcd(a,b)
# print("Нод =",d)
# k = (a * b) / d
# print("Нок =",k)

    ### Hard A ###
# while True:
#     num = int(input("Введите число: "))
#     if num < 2:
#         print("Common")
#     else:
#         for i in range(2, num):
#             if num / 1 == num and num %  i == 1 and num / 1 == num:
#                 print("Prime")
#                 break
#             else:
#                 print("Common")
#                 break
#     wrd = input("продолжаем(да/нет)? ")
#     if wrd == 'да' or wrd == 'Да' or wrd == 'ДА':
#         continue
#     else:
#         print("Goodbye!")
#         break

    ### Hard B ###
# y = 0
# num = int(input("Введите число: "))
# for i in range(num):
   
#     wrd = input("Введите букву: ")
#     x = ord(wrd) - 96
#     print("расположение в алфавите: ", x)
#     y += x
# print("Сумма букв алфавита: ",y)
