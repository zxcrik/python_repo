# age = int(input("Введите свой возраст: "))
# while age < 21:
#     print("Вам сюда нельзя")
#     age += 1

# print("\nконец программы ")
# print(age)

### оператор Break ###
# i = 0
# while i < 6:
#     print(i ,"decode")
 
#     if i == 4:
#         break   # досрочная остоновка цикла
#     i += 1

# ### Оператор Continue ###
###  при срабатывании Continue, весь код в блоке  
# z = 10
# while z > 0:
#     z -= 1            #если число четное 
#     if z % 2 != 0:
#         continue
#     print(z)

### Бесконечный цикл ###
# i = 0
# while i < 5:          ### случайный бесконечный цикл
#     print("decode")

# while True:           ### Намеренный бесконечный цикл
#     print("decode")


        ### Easy ###
### Problem A ###
# num = int(input("Введите число: "))
# i = 0
# while i < num:
#     print("decode")
#     i += 1

### Problem B ###
# num = int(input("Введите число: "))
# i = 1
# summa = 0
# while i <= num:
#     summa += i
#     print(summa)
#     i += 1

# ### Problem C ###
# l = int(input("Введите первое число: "))
# r = int(input("Введите второе число: "))
# while l <= r:
#     r -= 1 
#     if r % 2 != 0:
#         continue
#     print(r)

### Medium A ###
# num = int(input("Введите число: "))
# while num > 1:
#     num /= 2 
#     print(num)
# if num == 1:
#     print("yes")
# else:
#     print("no")

### Medium B ###
# n = int(input("Введите число: "))
# c = str(n)
# num = list(map(int, c))
# print(sum(num))

### Medium C ###
# n = float(input("Введите число: "))
# s = 0
# while n >= 1:
#         n = n / 2
#         print(n)
#         s += 1
#         print(s)

### Hard A ###
# a = int(input("Введите число: "))
# b = int(input("Введите число: "))
# f = 0
# n = b // a
# if b == a:
#     print("0")
# else:
#     while f != n:
#         f += 1
#         print(n)
#         if f < n:
#                 break

### Hard B ###
# import math
# ric = list(map(int,input('Введите значения через пробел: ').split()))
# while sum(ric) == 0:
#     ric.append(5)
#     print(ric)
#     if sum(ric) != 0:
#         break
# hip = pow(ric[0],2)  
# pou = pow(ric[1],2)  
# ged = pow(ric[2],2)  
# deb = pow(ric[3],2)  
# iou = pow(ric[4],2)   
# qrt = pow(ric[5],2)
# print(hip + pou + ged + deb + iou + qrt)
