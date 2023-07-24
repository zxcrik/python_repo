    ## Easy A ###
# st = input("Введите слова через пробел: ")
# print(len(st.split()))

    ### Easy B ###
# st = input("Введите строку: ")
# a = input("Введите символ который нужно заменить: ")
# b = input("Введите каким символом заменить: ")

# print(st.replace(a, b))

    ### Medium A ###
# st = input("Введите строку: ")
# center = len(st) // 2 + len(st) % 2
# a = len(st)
# while len(st) % 2 == 0:
#     st_1 = st[:len(st)//2]
#     st_2 = st[len(st)//2:]
#     print(s := (st_2 + st_1))
#     break
# else:
#     st_1 = st[:(len(st)//2)+1]
#     st_2 = st[(len(st)//2)+1:]
#     print(s := (st_2 + st_1))    
# 
# if len(st) % 2 != 0:
#   center += 1
# print(st[center:] + st[:center])
# 
# 

    ### Medium B ###
# st = input("Введите строку: ")

# for i in st: 
#     print(ord(i), end = "")

    ### Hard A ###
# st = input("Введите строку: ")
# st = st.lower()

# for j in st:
#     num = ord(j) - ord('a') + 1 
#     print(f"Алфавитный порядок буквы: '{j}' is {num}")

# for letter in st:
#   print(letter + ":", ord(letter.lower()) - 96)   или же  print(letter + ":", ord(letter.upper()) - 64)

    ### Hard B ###
# st = input("Введите строку: ")
# words = st.split()

# for word in words:
#     size = len(word)
#     print(f"Размер '{word}': {size}")
