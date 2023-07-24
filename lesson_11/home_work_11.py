    ### Easy A ###
# num = set(map(int, input("Введите числа через пробел: ").split()))
# xy = int(input("Введите делитель: "))

# ist = {x for x in num if x % xy != 0}                        # Нельзя изменять множество во время итерации # 
# print(ist)

    ### Easy B ###
# import math
# num = set(map(int, input("Введите числа через пробел: ").split()))
# set_1 = {x for x in num if x > 0 and (x & (x - 1)) == 0}
# print(set_1)

# 2 - Вариант решения #
# num = set(map(int, input("Введите числа через пробел: ").split()))
# ans = set()
# for el in num:
#     num = el
#     while el >= 1:
#         if el == 1:
#             ans.add(num)
#         el /= 2
# print(ans)

    ### Medium A ###
# num = set(map(int, input("Введите числа через пробел: ").split()))
# print("Максимальный элемент -",max(num))
# print("Минимальный элемент -",min(num))

    ### Medium B ###
# ls = list(map(int, input("Введите числа через пробел: ").split()))
# ls = set(ls)
# print("Различных чисел: ",len(ls))

    ### Hard A ###
# set_1 = set()
# intg = int(input("Введите кол - во чисел: "))
# cnt = 0

# while intg != cnt:
#     num = int(input("Введите число: "))
#     if num in set_1:
#         print("YES")
#     else:
#         print("NO")
#         set_1.add(num)
#     cnt += 1

# 2 - способ решения #
# numbers = list(map(int, input().split()))
# st = set()

# for el in numbers:
#     if el in st:
#         print("YES")
#     else:
#         print("NO")
#         st.add(el)

    ### Hard B ###
# num = int(input("Введите число строк: "))  
# words = set()  

# for i in range(num):
#     line = input("Введите строку: ").split()
#     words.update(line)

# print(len(words))

# 2 - способ решения #

# n = int(input())
# st = set()

# for i in range(n):
#     text = input()
#     words = text.split()
#     st.update(words)