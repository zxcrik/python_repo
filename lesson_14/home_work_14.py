    ### Easy A ###
# n = int(input("Введите кол-во строк: "))
# m = int(input("Введите кол-во чисел в строке: "))
# num = []

# for c in range(n): 
#     xy = list(map(int, input("Введите строку: ").split()))   
#     num.append(xy)

# max_val = num[0][0]
# max_row, max_col = 0, 0

# for i in range(n):
#     for j in range(m):
#         if num[i][j] > max_val:
#             max_val = num[i][j]
#             max_row, max_col = i, j
#         elif num[i][j] == max_val and (i < max_row or (i == max_row and j < max_col)):
#             max_row, max_col = i, j

# print(f"{max_row} : {max_col}")

    ### Medium A ###
# n = int(input("Введите кол-во строк: "))
# m = int(input("Введите кол-во чисел в строке: "))
# num = []

# for c in range(n): 
#     x = list(map(int, input("Введите числа в строку: ").split()))   
#     num.append(x)

# for i in range(n):
#     num[i] = num[i][::-1]
# num = num[::-1]

# for row in num:
#     print(*row)

    ### 2 - способ решения ###
# n = int(input("Введите кол-во строк: "))
# m = int(input("Введите кол-во чисел в строке: "))
# num = []

# for c in range(n): 
#     x = list(map(int, input("Введите числа в строку: ").split()))   
#     num.append(x)

# for row in num[::-1]:
#     print(*row[::-1])

    ### Hard A ###
# n = int(int(input("Введите размерность матрицы: ")))
# a = [[0 for i in range(n)] for j in range(n)]

# for i in range(0,n):
#     for j in range(0,n):
#         a[i][j] = '.'
# if n % 2 != 0:
#     for i in range(0,n):
#         for j in range(0,n):
#             a[i][i] = '*'      # Главная диагональ #
#             a[n - 1 - j][j] = '*'  # Побочная диагональ #
#             a[i][n // 2] = '*'     # Вертикальная диагональ #
#             a[n // 2][j] = '*'      # Горизонтальная диагональ #
#             print(a[i][j], end = " ")
#         print()
# else:
#     print("Введите не четное число !")

# def my_abc(number: int|float) -> int|float:
