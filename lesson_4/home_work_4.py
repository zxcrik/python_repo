   ### Problem C ###
# def phone_number(number: int) -> str:
#    c = str(number)
#    d = list(map(int, c))
#    if len(d) == 11:
#       print("Номер введен правильно")
#       if (d[1] == 7 and d[2] == 2 and d[3] == 7):
#          print("Ваш абонент: Active")
#       if (d[1] == 7 and d[2] == 0 and d[3] == 0) or (d[1] == 7 and d[2] == 0 and d[3] == 8):
#          print("ваш абонент: Altel 4g")
#       if (d[1]== 7 and d[2] == 0 and d[3] == 5) or (d[1] == 7 and d[2] == 7 and d[3] == 1) or (d[1] == 7 and d[2] == 7 and d[3] == 6) or (d[1] == 7 and d[2] == 7 and d[3] == 7):
#          print("Ваш абонент: Beeline")
#       if (d[1]== 7 and d[2] == 0 and d[3] == 1) or (d[1] == 7 and d[2] == 0 and d[3] == 2) or (d[1]== 7 and d[2] == 7 and d[3] == 5) or (d[1] == 7 and d[2] == 7 and d[3] == 8):
#          print("Ваш абонент: Kcell")
#       if (d[1]== 7 and d[2] == 0 and d[3] == 7) or (d[1] == 7 and d[2] == 4 and d[3] == 7):
#          print("Ваш абонент: Tele2")
#    else:
#       print("Номер введен не правильно")
# print("Определение абонента номера телефона\nПрограмма поможет определить абонент в рамках Казахстана ")
# print("Просaим вас ввести номер в числовом формате")
# number = int(input("Введите свой номер: "))
# (phone_number(number))

   ### Problem D ###
# print("Консольный калькулятор\nЗдесь вы сможете делать простые математические операции")
# integer_1 = float(input("Введите первое число: "))
# operations = ('+' , '-', '*', '/', '**' , '//', '%')
# print(operations)
# ope = input("Введите операцию: ")
# integer_2 = float(input("Введите второе число: "))
# if ope == '+':
#    print("Результат:\n",integer_1, "+" , integer_2 ," = ",integer_1 + integer_2)
# if ope == '-':
#    print("Результат:\n",integer_1, "-" , integer_2 ," = ",integer_1 - integer_2)
# if ope == '*':
#    print("Результат:\n",integer_1, "*" , integer_2 ," = ",integer_1 * integer_2)
# if ope == '/' and integer_2 != 0:
#    print("Результат:\n",integer_1, "/" , integer_2 ," = ",integer_1 / integer_2)
# elif ope == '/' and integer_2 == 0:
#    print("на ноль делить нельзя ")
# if ope == '**':
#    print("Результат:\n", "квадрат первого числа = " , integer_1 ** 2 ,"\n квадрат второго числа = ", integer_2 ** 2)
# if ope == '//' and integer_2 != 0:
#    print("Результат:\n","Целочисленное деление: ", integer_1, "//" , integer_2 ," = ",integer_1 // integer_2)
# elif ope == '//' and integer_2 == 0:
#    print("на ноль делить нельзя")
# if ope == '%' and integer_2 != 0:
#    print("Результат:\n","Деление с остатком: ", integer_1, "%" , integer_2 ," = ",integer_1 % integer_2)
# elif ope == '%' and integer_2 == 0:
#    print("на ноль делить нельзя")