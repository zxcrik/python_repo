    ### Easy A ###
# a = []
# num = int(input("Введите размерность списка: "))
# for df in range(num):
#     wr = input("Введите элементы: ")
#     a.append(wr)
# print(a)

# ls = list(map(eval,input().split()))
# print(ls)

    ### Easy B ###
# numbers = []
# num = int(input("Введите размерность списка: "))

# for i in range(num):
#     ab = int(input("Введите числа: "))
#     if ab % 2 != 0:
#         numbers.append(ab)

# print(*numbers)


    ### Medium A ###
# numbers = []
# num = int(input("Введите размерность списка: "))

# for i in range(num):
#     ab = int(input("Введите числа: "))
#     numbers.append(ab)

# print("Максимальный элемент: ",max(numbers))
# print("Индекс макс.элемента: ",numbers.index(max(numbers)))


    ### Medium B ###
# numbers = []
# num = int(input("Введите размерность списка: "))

# for i in range(num):
#     ab = int(input("Введите число: "))
#     numbers.append(ab)
# print(numbers)

# m = int(input("Введите число m: "))
# print("Кол - во вхождения элемента m в массиве: ",numbers.count(m))


    ### Hard A ###
# numbers = []
# num = int(input("Введите размерность списка: "))

# for i in range(num):
#     ab = int(input("Введите число: "))
#     numbers.append(ab)
# print("Изначальный список: ",*numbers)

# c = numbers.index(min(numbers))
# d = numbers.index(max(numbers))
# numbers[c] , numbers[d] = numbers[d],numbers[c]
# print("Измененный список: ",*numbers)

    ### Hard B ###
# numbers = list(map(int,input("Введите числа: ").split()))
# cnt = 0

# for i in range(len(numbers)):
#     for j in range(i + 1, len(numbers)):
#         if numbers[i] == numbers[j]:
#             cnt += 1
# print("Пар из  введеных чисел: ",cnt)


  