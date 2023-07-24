    ###  Set(Множество)  Frozenset(Не изменяемое множество) ###
# ls = [1,1,2,3]
# print(ls)

# st = {1,1,2,3}
# print(st)

# ls = ["python", "c++", "js"]
# print(ls)

# ls = {"python", "c++", "js"}  set используется для оптимизации  (алгоритм set ставит элементы по разным формулировкам)
# print(ls)

    ### Как создать пустой сет ? ###
# st = set()
# print(type(st))
# print(len(st))

# st = {1,2,3}
# print(type(st))
# print(len(st))

    ### Итерация ###   (только одна)
# st = {"python", "c++", "js"} 

# for el in st:
#     print(el)

    ### Проверка элемента ###
# print("c++" in st)
# print("python" not in st)

    ### Методы ###
### .add() ### (добавить элемент)
# st = {"a", "b", "c"}
# st.add("z")
# print(st)

### .remove() .discard() ###
# st = {"a", "b", "c"}
# st.remove("b")  Создание строгости (для визуализации ошибок)
# st.discard("k")
# print(st)

### .pop() ### Удаляет случайный элемент
# st = {"a", "b", "c"}
# delected = st.pop()
# print(st)
# print(delected)


# online = {"alan", "erlan", "qairat", "dima"}
# offline = {"erlan", "lesha", "alan", "taman"}

### .union() .update() ###
# print(online.union(offline))    Объединение сетов в один
# online.update(offline)

    ### .intersection() / пересечение одинаковых элементов ###
# print(online.intersection(offline))
# online.intersection_update(offline)
# print(online)

    ### .differents() / отличие ###
# online = {"alan", "erlan", "qairat", "dima"}
# offline = {"erlan", "lesha", "alan", "taman"}

# print(online.difference(offline))    
# print(offline.difference(online))

    ### .symmetric_difference() ###    объединение элементов которые не встречаются 
# print(online.symmetric_difference(offline))

    ### .issubset()  .issuperset ###   (Является ли сет частью набора чего - то)
# languages = {"python", "c++", "js", "java", "c#", "c" , "go"}
# c_languages = {"c#", "c++", "c"}
# print(c_languages.issubset(languages))

    ### input() ###
# x = set(input().split())
# print(x)

# numbers = set(map(int, input().split()))     Ввод множества 
# print(numbers)

    ### Easy A ###
# set_1 = {10,20,30,40,50}    
# set_2 = {30,40,50,60,70}
# print(set_1.union(set_2))

    #### Easy B ###
# set_1 = {10,20,30,40,50}    
# set_2 = {30,40,50,60,70}
# print(set_1.intersection(set_2))

    ### Easy C ###
# set_1 = {10,20,30,40,50}    
# set_2 = {30,40,50,60,70}
# print(set_2.difference(set_1))
# print(set_1.difference(set_2))

    ### Easy D ###
# print(text := set(input().split()))

    ### Medium A ###
# text = input()
# print(len(set(text)))
# print(set(text))

    ### Medium B ###
# n = int(input("Кол-во слов в предложении: "))
# cnt = 0
# sr = set()
# set_1 = set()


# while n != cnt:
#     text = input("Введите имя: ")
#     cnt += 1
#     sr.add(text)
# print(n - len(sr))

    ### Medium C ###
# num = int(input("Введите число: "))
# digits = []

# while num != 0:
#     digits.append(num % 10)
#     print(num)
#     num //= 10
# digits = set(digits)
# print(sorted(digits))

    ### Hard A ###
# text = input("Введите текст: ")

# text = set(text)
# text.discard(" ")
# text.discard(",")
# text.discard(".")
# text.discard("-")
# text.discard("!")

# for i in text:
#     text = list(text)
#     text.sort(reverse = True)
# print(*text)

    ### Hard C ###
# text = input("Введите текст: ")
# duplicates = set(x for x in text if list(text).count(x) > 1)
# non_repeated = set(x for x in text if list(text).count(x) == 1)
# text = set(text)
# text.discard(" ")
# text.discard(",")
# text.discard(".")
# text.discard("-")
# text.discard("!")

# print(non_repeated)
# print(duplicates)
