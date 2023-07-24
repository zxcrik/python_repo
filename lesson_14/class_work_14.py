    ### Двумерные массивы ###
# numbers = [
#     [1,2,3,4],      # Линия / дорожка #
#     [4,5,6,7],
#     [8,9,10,11]
# ]
# print(len(numbers))   # 3 #

# print(numbers[1][-1])  # 7 #

    ### Итерация ###
# for row in numbers:             # Пробежка по линиям #
#     for el in row:          # пробежка по спискам линий #
#         print(el * 2, end = " ")
#     print()

    ### Пробежка по индексам #
# for i in range(len(numbers)):
#     for j in range(len(numbers[i])):
#         print(i , j, sep = ":")

    ### Самый короткий принт ###
# for row in numbers:          # В виде таблицы #
#     print(*row)     

    ### Сумма ###
# summa = 0
# for row in numbers:
#     summa += sum(row)
# print(summa)

    ### Генерация ###
# n = [[0] * 3 for i in range(3)]
# n[0][1] = 5

# for row in n:
#     print(*row)

    ### input() ###
# n,m = map(int , input().split())   # 2 числа в одном input #
# numbers = []

# for i in range(n): 
#     x = list(map(int, input().split()))[:m]   # ограничение 
#     numbers.append(x)
# print(*numbers)

    ### Пример 1 ###
# n = int(input("Размер матрицы: "))    
# matrix = [['x'] * n for i in range(n)]

# for i in range(len(matrix)):
#     for j in range(len(matrix[i])):
#         if i == j:
#             matrix[i][j] = 1
#         elif i > j:
#             matrix[i][j] = 2
#         else:
#             matrix[i][j] = 0

# for row in matrix:
    # print(*row)

    ### Пример 2 ###
# n = [[0] * 4 for i in range(4)]
# r = 1

# for i in range(len(n)):
#     for j in range(len(n[i])):
#         n[i][j] = i * j

# for row in n:
#     print(*row)

    ### Easy A ###
# ls = [[1,5,9], [8,5,2],[3,6,7]]
# for row in ls:
#     print(*row)

#     ### Easy B ###
# numbers = []
# for i in range(2):
#     n = list(map(int, input("Введите числа: ").split()))
#     numbers.append(n)
# print(*numbers)

    ### Easy C ###
# n = int(input("Введие размер матрицы: "))
# mat = []
# cnt = 0

# for c in range(n):
#     x = list(map(int, input("Введите числа: ").split()))
#     mat.append(x)


# for i in range(len(mat)):
#     for j in range(len(mat[i])):
#         if mat[i][j] < 0:
#             cnt += 1 
# print(cnt)

    ### Easy D ###
# n = int(input("Введите кол-во строк: "))
# m = int(input("Введите кол-во чисел в строке: "))
# matr = [[0] * m for i in range(n)]
# num = []

# for c in range(n): 
#     x = list(map(int, input("Введите строку: ").split()))   
#     num.append(x)
#     num[c].reverse()

# for row in num:
#     print(*row)

    ### Medium A ###
# n = int(input("Введите кол-во строк: "))
# m = int(input("Введите кол-во чисел в строке: "))
# matr = [[0] * m for i in range(n)]
# num = []

# for c in range(n): 
#     x = list(map(int, input("Введите строку: ").split()))   
#     num.append(x)

# for i in range(len(num)):
#     for j in range(len(num[i])):
#         if num[i][j] % 2 == 0:
#             num[i][j] += 1
            
#         if num[i][j] % 2 != 0:
#             num[i][j] -= 1
        
# for row in num:
#     print(*row)

    ### Medium B ###
# n = int(input("Введите кол-во строк: "))
# m = int(input("Введите кол-во чисел в строке: "))
# matr = [[0] * m for i in range(n)]
# num = []

# for c in range(n): 
#     x = list(map(int, input("Введите строку: ").split()))   
#     num.append(x)

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

    ### Medium C ###
# n = 8
# m = 8
# mr = [['#'] * m for i in range(n)]
# cnt = int(input("Введите кол-во мин: "))

# for i in range(cnt):
    # kr_1 = int(input("Введите  i координату: "))
    # kr_2 = int(input("Введите  j координату: "))
    # mr[kr_1][kr_2] = '%'

#     if mr[kr_1][kr_2] == '%':
#         mr[kr_1][kr_2] = '@'  
#         mr[kr_1 + 1][kr_2] = '@' 
#         mr[kr_1 - 1][kr_2] = '@'  
#         mr[kr_1][kr_2+1] = '@'  
#         mr[kr_1][kr_2 - 1] = '@'
# for row in mr:
#     print(*row) 

    ### Hard A ###
# n = int(input("Введите не четное число: "))
# mr = [['.'] * n for i in range(n)]
# kr1 = int(input("Введите i координату: "))
# kr2 = int(input("Введите j координату: "))
# mr[kr1][kr2] = 'R'

# for i in range(0,n):
#     if mr[kr1][i] != 'R':
#         mr[kr1][i] = '!'
#     if mr[i][kr2] != 'R':
#         mr[i][kr2] = '!'

# mr[kr1][kr2] = 'R'
# for row in mr:
#     print(*row)

    ### Hard B ###
# n = int(input("Введите четное число: "))
# rt = [['.'] * n for i in range(n)]
# kr1 = int(input("Введите i координату: "))
# kr2 = int(input("Введите j координату: "))
# rt[kr1][kr2] = 'R'

# for i in range(0,n):
#     if rt[kr1 // 2][i] != '!':
#         rt[kr1 // 2][i] = '!'
#     if rt[i][kr2 // 2] != '!':
#         rt[i][kr2 // 2] = '!'
#     if rt[i][i] != '!':
#         rt[i][i] = '!'
#     if rt[i][n-1-i] != '!':
#         rt[i][n-1-i] = '!'
# rt[kr1][kr2] = 's'
# for row in rt:
#     print(*row)
