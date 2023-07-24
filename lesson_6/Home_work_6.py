from random import randint , choise , randrange, choices
#randrange(0,100,2) 2 , 4 ,6 , 8 
# choise(["да" , "нет"])   выбирает из списка один элемент
# choices(["yes","no"])     выбирает из списка несколько элементов

# print("Шарик с предказаниями!\nКаждый раз будет выдавать случайное предсказание.")
# print("А так же можете задать свой вопрос и получить ответ.")
# print("Режимы:\n1)предсказание.\n2)Задать вопрос.")
# from random import randint, choice
# print("1) Предсказание\n2) Задать вопрос\n")

# while True:
#     human_choice = int(input("Выберите режим: "))

#     if human_choice == 1:
#         x = randint(1, 4)
#         if x == 1:
#             print("Бдует плохаяа погода")
#         elif x == 2:
#             print("У вас будет удачный день")
#         elif x == 3:
#             print("Вам кто-то навредит!")
#         else:
#             print("Будет прибыльный день!")
#     elif human_choice == 2:
#         input("Задайте свой вопрос: ")
#         # x = randint(1, 2)
#         # if x == 1:
#         #     print("Ответ: Да")
#         # else:
#         #     print("Ответ: Нет")
#         print(choice(["Да", "Нет", "Не знаю"]))
#     else:
#         print("Вы сделали некорректный выбор!")

#     print()
#     ans = input("Хотите продолжить? (y/n): ")
#     if ans == "n" or ans =="N":
#         print("Goodbye!")
#         break

#     print()

    ### Problem D ###
# print("КОНСОЛЬНЫЙ КАЛЬКУЛЯТОР")
# print("Здесь вы сможете делать простые вычесления! ")
# print('-' * 30)
# wrd = str(1)
# while True:
#     integer_1 = float(input("Введите первое число: "))
#     operations = ('+' , '-', '*', '/', '**' , '//', '%')
#     print(operations)
#     ope = input("Введите операцию: ")
#     integer_2 = float(input("Введите второе число: "))
#     if ope == '+':
#         print("Результат:\n",integer_1, "+" , integer_2 ," = ",integer_1 + integer_2)
#     if ope == '-':
#         print("Результат:\n",integer_1, "-" , integer_2 ," = ",integer_1 - integer_2)
#     if ope == '*':
#         print("Результат:\n",integer_1, "*" , integer_2 ," = ",integer_1 * integer_2)
#     if ope == '/' and integer_2 != 0:
#         print("Результат:\n",integer_1, "/" , integer_2 ," = ",integer_1 / integer_2)
#     elif ope == '/' and integer_2 == 0:
#         print("на ноль делить нельзя ")
#     if ope == '**':
#         print("Результат:\n", "квадрат первого числа = " , integer_1 ** 2 ,"\n квадрат второго числа = ", integer_2 ** 2)
#     if ope == '//' and integer_2 != 0:
#         print("Результат:\n","Целочисленное деление: ", integer_1, "//" , integer_2 ," = ",integer_1 // integer_2)
#     elif ope == '//' and integer_2 == 0:
#         print("на ноль делить нельзя")
#     if ope == '%' and integer_2 != 0:
#         print("Результат:\n","Деление с остатком: ", integer_1, "%" , integer_2 ," = ",integer_1 % integer_2)
#     elif ope == '%' and integer_2 == 0:
#         print("на ноль делить нельзя")
#     wrd = input("продолжаем(да/нет)? ")
#     if wrd == 'да' or wrd == 'Да' or wrd == 'ДА':
#         continue
#     else:
#         print("Good bye")
#         break