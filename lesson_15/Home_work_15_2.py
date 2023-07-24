    ### Problem C ###
# def is_power_two(x: int) -> str:
#     while x > 1:
#         x /= 2 
#     if x == 1:
#         return ("yes")
#     else:
#         return ("no")     
# x = int(input("Введите число: "))
# print(is_power_two(x))

    ### Problem B ###
# def str_sort(s: str) -> str:
#     return sorted(s)
# s = input("Введите строку: ")
# print(*str_sort(s), sep = "")

    ### Problem A ###
# def best_movies(n: int) -> str:             # n - количество;  fil - Фильмы ; rt - Рейтинг #
#     cnt = 0
#     fl = []
#     rati = []
#     while cnt != n:
#         fil = input("Введите фильм: ")
#         rt = float(input("Введите оценку IMDB: "))
#         fl.append(fil)
#         rati.append(rt)
#         cnt += 1
#     top_movies = []
#     d = dict(zip(fl,rati))
#     for k , v in d.items():
#         if v > 7:
#             top_movies.append(k)
#     if not top_movies:
#         return "Нет фильмов с оценкой выше 7"
#     else:
#         return top_movies
# n = int(input("Введите кол-во фильмов: "))
# print(*best_movies(n))



