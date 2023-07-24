    ### Easy A ###
# ms = list(map(int, input("Введите список чисел: ").split()))

# for i in range(1,len(ms)):
#     if ms[i] > ms[i-1]:
#         print(ms[i], end = " ")

    ### Easy B ###
# ms = list(map(int, input("Введите список чисел: ").split()))
# even = []
# for el in ms:
#     if el % 2 == 0:
#         even.append(el)

# if len(even) == 0:
#     print("Error")
# else:
#     print(max(even))

    ### 2 - способ решения ###
# print(str(ms := list(map(int, input("Введите список чисел: ").split()))) * 0, max(ms) if max(ms) % 2 == 0  else ("error"))

    ### Medium A ###
# d = {
#     "OOP" : [81,88,72,97],
#     "ICT" : [78,69,86,98],
#     "Math" : [65,69,78,98],
#     "Physics" : [87,99,66,70]  
# }
# it = []
# gr = []

# for k , v in d.items():
#     it.append(k)
#     gr.append(sum(v) / len(v))
# print(dd := dict(zip(it,gr)))

    ### 2 способ решения ###
# for k , v in d.items():
#     d[k] = sum(v) / len(v)
# print(d)

    ### Medium B ###
# st = input("Введите строку: ")
# sym = input("Введите специальный символ: ")
# sta_in = st.find(sym)
# if sta_in == -1:
#     print(f"Символ {sym} не найден")
#     exit()
# end_in = st.find(sym, sta_in + 1)
# if end_in == -1:
#     print(f"Второй символ {sym} не найден в строке")
#     exit()

# bef = st[:sta_in + 1]
# aft = st[end_in:]

# pr_st = st[sta_in + 1: end_in]
# revers = pr_st[::-1]
# print(new_st := bef + revers + aft)

    ### Hard A ###
# lis = list(map(int, input("Введите список чисел: ").split()))
# n_ch = []


# for i in lis:
#     if i % 2 != 0 and i > 0:
#         n_ch.append(i)

# if not n_ch:
#         print("Error")
# else:
#     mx = max(n_ch)
#     print("Число:",mx ,"Сумма:",(mx // 10) + (mx % 10))

    ### Hard B ###
# py = []
# c = []
# cpt = 0   
# cct = 0
# l_py = int(input("Число занимающихся python: "))
# lc = int(input("Число занимающихся C++: "))

# while l_py != cpt:
#     name_py = input("Введите ученика занимающегося python: ").title()
#     py.append(name_py)
#     cpt += 1

# while lc != cct:
#     name_c = input("Введите ученика занимающегося c++: ").title()
#     c.append(name_c)
#     cct += 1
# py.extend(c)

# for i in py:   
#     if py.count(i) >= 2:
#         while py.count(i) != 0:
#             py.remove(i)
#         print("Учеников изучающих один язык: ",len(py))
#         break
#     else:
#         print("Учеников изучающих один язык: ",len(py))
#         break
        
    ### 2 способ решения ###
# a,b = int(input("CPP: ")), int(input("python: "))
# cpp, python = set(), set()

# for i in range(a):
#     name = input()
#     cpp.add(name)

# for i in range(b):
#     name = input()
#     python.add(name)

# print(len(cpp.symmetric_difference(python)))
