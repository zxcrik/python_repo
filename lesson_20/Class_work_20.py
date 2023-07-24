    ### Easy A ###
# import re
# text = input("Введите строку: ")
# res = re.sub(r"[0-9]", r"",text)
# print(res)

    ### Easy B ###
# import re
# text = input("Введите строку: ")
# res = re.split(r'[,.!]',text)
# print(res)

    ### Easy C ###
# import re
# text = input("Введите строку: ")
# res = bool(re.search(r"^The",text))
# if res == True:
#     print("Нашел совпадение!")
# else:
#     print("Не нашел совпадение!")

    ### Medium A ###
# import re
# text = input("введите строку: ")
# res = re.search(r"decode", text, flags = re.IGNORECASE)
# if res:
#     print(res.span())
# else:
#     print("Совпадений нет!")

    ### Medium B ###
# import re
# text = input("Введите доменны: ")
# res = bool(re.search(r"(http|https)://[a-zA-Z]+\.[a-zA-Z]+/?", text))
# print(res)

    ### Medium C ###
# import re
# text = input("Введите строку: ")
# res = re.findall(r"[A-Z][a-z]+",text)
# print(res)

    ### Hard A ###
# import re
# g_mail = input("Введите почту: ")
# res = bool(re.search(r"^[a-z0-9_.]+@[a-z]{2,6}\.[a-z]{2,4}$", g_mail))
# if res:
#     print("send me meme")
# else:
#     print("uh?")

    ### Hard B ###
# import re
# number = input("введите тел.ном: ")
# res = re.search(r"^(?:\+7|8)?[\s-]?\(?[489][0-9]{2}\)?[\s-]?[0-9]{2}[\s-]?[0-9]{2}$", number)        
# if res:                                 # ! #
#     print("+7 (702) 512 24-49")
# else:
#     print("what is this? ")   