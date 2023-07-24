    ### Easy A ###
# a = int(input("Введите число: "))
# b = int(input("Введите число: "))
# ls_1 = []
# ls_2 = []

# for i in range(a, b+1):
#     ls_1.append(i)
#     ls_2.append(i ** 2)

# print(dict(zip(ls_1, ls_2)))

    ### Easy B ###
# d = {
#     "OOP":[77,88,99,66],
#     "ICT":[100,98,99,96]
# }

# for  val in d["OOP"]:
#     print(f"OOP: {val}")

# for valu in d["ICT"]:
#     print(f"ICT: {valu} ")

    ### 2 - способ решения ###
# for k,v in d.items():
#     for el in v:
#         print(k + ":", el)

    ### Medium A ###
# st = input("Введите строку: ").split()
# di = dict.fromkeys(st,-1)

# for mi_st in st:
#     di[mi_st] += 1
# print(*di.values())

    ### Medium B ###
# s = input("Введите строку: ")
# s = s.replace(' ','')
# di = dict.fromkeys(s,0)     

# for mi_s in s:
#     di[mi_s] += 1
# print(di)

    ### Hard A ###
# countries = {
#     'Kazakhstan' : ['Almaty', 'Nur - Sultan', 'Shymkent'] ,
#     'Ukraine' : ['Kiev', 'Donetsk', 'Odessa']
# }

# city = input("Введите название города: ").title()

# for country , cities in countries.items():
#     if city in cities:
#         print(f"{city} находится в стране {country}")
#         break
#     else:
#         print(f"Для города {city} не найдена страна в нашем списке")

    ### Hard B ###
# n = int(input("Введите число синонимов: "))
# cnt = 0
# ls_1 = []
# ls_2 = []

# while n != cnt:
#     a = input("Введите 1 синоним: ")
#     b = input("Введите 2 синоним: ")
#     ls_1.append(a)
#     ls_2.append(b)
#     cnt += 1

# di = dict(zip(ls_1, ls_2))
# synon = input("Введите синоним: ")
# found = False

# for key , valu in di.items():
#     if synon in valu:
#         print(f"Синоним {synon} - {key}")
#         found = True
#         break
#     elif synon in key:
#         print(f"Синоним {synon} - {valu}")
#         found = True
#         break
# if not found:
#     print(f"Синонима {synon} - здесь нет!")
        
### 2 variant ###

# dt = {}

# n = int(input())
# for i in range(n):
#     first, last = input().split()

#     dt[first] = last
#     dt[last] = first


# word = input()
# print(dt[word])
