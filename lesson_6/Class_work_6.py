#     ### Problem A ###
# from random import randint
# print("Угадайте число\n Случайное число находится между 1 и 100\n У вас неограниченное кол-во попыток")
# print("Игра начинается...")
# x = randint(1,100)
# num = 0
# cnt = 0
# while num != x:
#     num = int(input("Введите число: "))
#     cnt += 1
#     if num != x:
#         print("попытка #", cnt,)
#         print("Вы не угадали,попробуйте еще")
#         if num < x:
#             print("Введенное вами число, ниже чем надо!")
#         else:
#             print("Введенное число, выше чем надо!")
#     else:
#         print("попытка #", cnt,)
#         print("Вы угадали!\n Количество попыток: ",cnt)  

    ## Problem B ###

# print("Камень-ножницы-бумага!")
# print("Вы будете играть с компьютером в игру \"су-ли-фа\".")
# print("Компьютер сделал уже свой выбор")
# print("Теперь ваша очередь...\n")

# print("1---Камень\n2---Ножницы\n3---Бумага\n")
# cnt_human = 0
# cnt_comp = 0

# while True:
#     print("-" * 30)
#     x = randint(1, 3)
#     answer = int(input("Сделайте свой выбор (1|2|3): "))

#     print()
#     if x == 1:
#         print("Выбор компьютера: Камень")
#     elif x == 2:
#         print("Выбор компьютера: Ножницы")
#     else:
#         print("Выбор компьютера: Бумага")

#     if answer == 1:
#         print("Ваш выбор: Камень")
#     elif answer == 2:
#         print("Ваш выбор: Ножницы")
#     else:
#         print("Ваш выбор: Бумага")


#     if x == answer:
#         print("Ничья")
#     elif (x == 1 and answer == 2) or (x == 2 and answer == 3) or (x == 3 and answer == 1):
#         cnt_comp += 1
#     else:
#         cnt_human += 1

#     print("Счет(Компьютер: " + str(cnt_comp) + ", Человек: " + str(cnt_human) + ")\n")

#     print()

#     if cnt_human == 3:
#         print("Вы выиграли игру!")
#         break
#     elif cnt_comp == 3:
#         print("Компьютер выиграл игру!")
#         break

