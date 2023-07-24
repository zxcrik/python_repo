    ### Строки ###
# text = "decode_5"

# print(text[3])
# print(text[-1])

### Slice(Срезы) ###
# print(text[2:6])
# print(text[:6])
# print(text[7:2:-1])

### Итерация ###
# text = "decode"
# for letter in text:  #V1
#     print(letter)
# for i in range(len(text)):  
#     print(i, text[i])

### Форматирование ###
# Вставка данных в строку #

# V1
# text = "https://www.{}.{:.5f}/"
# print(text.format("decode", "kz"))
# print(text.format("google", "com"))
# print(text.format(5, 3.2))
# V2 f - string  f - строка
# number = 0
# print(f"Попытка #{number}:")

# V3
# text = "My name is %s, I'm %i years old!"
# name = "John"
# age = 36
# print(text % (name, age))

    ### Методы строки ###
## .lower()   .upper() ##
# text = "DeCode_5"
# print(text.lower())
# print(text.upper())

## .islower()  .isupper() .isalpha() ##
# text = "DeCode"
# print(text.islower())
# print(text[0].islower())
# print(text[-1].isalpha())

## .isdigit() ##
# text = input()
# print(text.isdigit())

## .count() ##
# text = "Decode"
# print(text.count("d"))

## .replace() ##
# text = "hecohe"
# print(text.replace("h","D"))
# print(text.replace("cohe", "code"))

# text = "decode school"
# print(text.replace("o", "0", 2))

## .index()  .find() ##
## .rindex() .rfind() ##
# text = "python"
# print(text.index("k"))
# print(text.find("k"))

# .strip() .lstrip() .rstrip() ##  Удаление пробелов
# text = input().strip()
# age = input("Введите число: ").strip()
# print(f"Ваше имя: {text}, Ваш возраст {age}")

## .title() .capitalize() ##   Поднятие первых букв
# text = "deCODE schOOl groUP"
# print(text.capitalize())
# print(text.title())

## .split() ##
# text = "1 2 2 3"
# print(text.split())
# data = "06/03/2023"
# print(data.split())

## .join() ##
# text = ["decode", "tyre", "gene"]
# print("/".join(text))
# time = [20,56,34]
# print(":".join(map(str, time)))

# print(eval("5 + 5"))


    ### Easy A ###
# sen_1 = input("Введите первого отправителя: ")
# sen_2 = input("Введите первого отправителя: ")

# if sen_1[0:] == sen_2[0:]:
#     print("yes")
# else:
#     print("no")

    ### Easy B ###
# st = input("Введите строку: ")
# print(st[::-1])

    ### Easy C ###
# st = input("Введите строку: ")
# num_1 = int(input("Введите начало среза: "))
# num_2 = int(input("Введите конец среза: "))
# print("Результат: ",st[num_1:num_2 + 1])

    ### Easy D ###
# st = input("Введите строку: ")
# num = int(input("Введите средний индекс строки: "))
# rtx = int(input("Ввежите последний индекс строки: "))
#
# for i in range(len(st)):
#     if i % 2 == 0: 
#         fg = st[0:num]
#         vb = st[num:rtx+1]                  
#     print(fg.lower() + vb.upper())
#     break

    ### Medium A ###
# stri = input("Введите строку: ").split()
# if stri.islower():
#     print(stri)
# else:
#     a = stri.find(stri.upper())
#     if a == 0:
#         print(stri[0].lower() + stri[1:].upper())
#     if a > 0 or a < -1:
#         print(stri[0:a].upper() + stri[a].lower() + stri[a:])
#     if a == -1:
#         print(stri[0:a].upper() + stri[a].lower())
#     print(a)

    ### Medium B ###
# s = input("Введите строку: ")
# a = sum(map(str.isupper, s))
# b = sum(map(str.islower, s))
# print(a * b)