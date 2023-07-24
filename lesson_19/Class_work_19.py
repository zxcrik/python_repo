    ### Регулярные выражения / regex #
import re
# print(bool(re.search("c", "decode"))) 

# ^ - начало строки #
# print(bool(re.search(r"^c", "decode"))) 

# $ - конец строки #
# file_name = input()
# print(bool(re.search(r".js$", file_name))) 

# ^ $ - от начала до конца #  

# \ - экранированние/ изоляция #
# text = input()
# print(bool(re.search(r"\$$", text)))      # изоляция представленного символа #

# [] - набор символов #
# text = input()
# print(bool(re.search(r"^[a-zA-Z0-9]", "text"))) 

# [^ ] - набор КРОМЕ
# text = input()
# print(bool(re.search(r"[^0-9]$", text))) 

# .- любой символ #
# text = input()
# print(bool(re.search(r"^a.b$", text))) 

# +  - 1 или более 
# text = input()
# print(bool(re.search(r"^[a-z_.0-9]+@", text)))  

# *  - 0 или более 
# text = input()
# print(bool(re.search(r"^[a-z_.0-9]*@", text)))  
  
# ? - будет или не будет
# text = input()
# print(bool(re.search(r"^\+?7", text))) 

# {}  - конкретное количество 
# text = input()
# print(bool(re.search(r"^[0-9]{2,4}[a-z]", text)))      # не ставить после пробела запятую #

# |  - или
# text = input()
# print(bool(re.search(r"^7|8|\+7", text))) 

# () - группировка
# text = input()
# result = re.search(r"([a-z]+)\.([a-z]+)", text)
# if result:
#     print(result.group(0))
#     print(result.group(1))
#     print(result.group(2))

### match() ###
# print(bool(re.match("c", "decode")))  # ищет только в начале #

### compile() ###
# text = input()
# pattern = re.search("([a-z]+)\.([a-z]+)", text)     
# result = re.search(pattern, text)
# print(result)

### findall() ###
# text = input()
# result = re.findall(r"\d+", text)            # находит все, что записано #
# print(result)

### split() ###
# text = input()
# result = re.split(r"\d+", text)
# print(result)

### sub() ###


# text = input()
# result = re.sub(r"([a-z]+)\.([a-z]+)", r"\2.\1" ,text)
# print(result)

# r"(+7 \d{3} \d{7})"   r"\1 *** ** ** "

# text = input()
# result = re.sub(r"[a-z]", r"_" ,text, flags=re.IGNORECASE)
# print(result)

# \b - пробел, пустая строка, и все что не ищется 
# import re
# text = input()    
# years = re.findall(r"\b\d{4}\b", text)
# print(years)

    ### Easy A ###
# text = input("Введите строку: ")
# res = bool(re.findall(r"[0-9]", text))
# print(res)

    ### Easy B ###
# st = input("Введите строку: ")
# pat = r"^[a-zA-Z0-9]+$"
# res = bool(re.search(pat, st))
# if res:
#     print("Нашел совпадение!")
# else:
#     print("Не нашел совпадение!")

    ### Easy C ###
# st = input("Введите строку: ")
# pat = r"^[a-z]+_[A-Z][a-z]+$"
# res = bool(re.search(pat, st))
# if res:
#     print("Нашел совпадение!")
# else:
#     print("Не нашел совпадение!")

    ### Medium A ###
# text = input("Введите строку: ")
# res = bool(re.search(r"[a-zA-Z0-9]+ cool$", text))
# print(res)

    ### Medium B ###
# st = input("Введите строку: ")
# res = re.search(r"^a[a-zA-Z0-9!#@$%&* ]+b$", st)
# if res:
#     print("Нашел совпадение!")
# else:
#     print("Не нашел совпадение!")

    ### Medium C ###
# user_ip = input("Введите ip - адрес: ")
# res = re.search(r"[0-9]{3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1}", user_ip)
# if res:
#     print("IP")
# else:
#     print("something else")