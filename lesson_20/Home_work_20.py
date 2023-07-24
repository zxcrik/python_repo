import re
    ### Easy A ###
# date = input("Введите дату: ")
# res = re.search(r"([0-9]{4})\/([0-9]{2}\/[0-9]{2} [0-9]{2}\:[0-9]{2})", date)
# if int(res.group(1)) < 1000 or int(res.group(1)) > 2012:
#     print("NO")
# else:
#     print("Yes")

    ### Easy B ###
# rgb = input("Введите цвет rgb: ")
# cl = re.search(r"([0-9]{1,3}),([0-9]{1,3}),([0-9]{1,3})", rgb)
# if int(cl.group(1)) == 192 and int(cl.group(2)) == 192 and int(cl.group(3)) == 192:
#     print("Серый цвет")
# elif int(cl.group(1)) == 255 and int(cl.group(2)) == 255 and int(cl.group(3)) == 255:
#     print("Белый цвет")
# elif int(cl.group(1)) == 0 and int(cl.group(2)) == 0 and int(cl.group(3)) == 0:
#     print("Черный цвет")
# else:
#     print("Другой цвет")

    ### Medium A ###
# st = input("Введите строку: ")
# res = re.search(r"\b(a)([a-zA-Z]+)(a)\b",st)
# if res:
#     result = re.sub(res.group(1) + '|' + res.group(3), "!", st)           # <- конкатенация и замена буквы a #
#     print(result)
# else:
#     print(res)

    ### Правильный метод решения #
# text = input("Введите строку: ")
# res = re.sub(r"a([^a\s]+)a", r"!\1!", text, flags = re.IGNORECASE)
# print(res)

    ### Medium B ###
# text = input("Введите текст: ")
# simb = input("Введите символ: ")
# print(f"Количество {simb} в строке: ", res := len(re.findall(simb, text, flags = re.IGNORECASE)) - 1)

    ### Hard A ###
# number = input("Введите номер: ")
# tele_2 = re.search(r"[+]7 (747|707) [0-9]{3} [0-9]{2} [0-9]{2}", number)
# if tele_2:
#     print("Hello?")
# else:
#     print("Declined")

    ### 2 - способ решения задачи #
# number = input("Введите номер: ")
# patt = r"^(\+7|8)(747|707)\d{7}$"
# if re.search(patt, number):
#     print("Hello?")
# else:
#     print("declined")