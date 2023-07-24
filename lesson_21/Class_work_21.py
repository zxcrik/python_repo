    ### Работа с файлами ###
### mod "x" ###
# try:
#     file = open("abc.java", "x")
# except FileExistsError:
#     print("Файл уже создан")
# else:
#     file.close()
#     print("Файл был создан")

### mod "r" ###
# file = open("db.txt", "r", encoding="utf-8")    # кодировка для работы с другими символами #
# method read() #    <- Все содержимое одной строкой 
# print(file.read())

# method readline() #    <-  Читает по одной линии 
# print(file.readline())
# print(file.readline())      # Читатется следующая строка #

# method readlines() #   <- Читает все линии, создает список 
# print(file.readlines())
# file.close()

 # читаемые файлы через - rt;    не читаемые - rb #
# file = open("db.txt", "rb")

    ### mode "a" ###               <- дозапись 
# file = open("db.txt", "a")

# file.write("c++\n")
# file.write("c#\n")
# file.write("css\n")

# file.close()

    ### mode "w" ###      <- перезапись 
# file = open("db.txt", "w")              # на этом моменте содержимое файла удаляется #

# file.write("c++\n")
# file.write("c#\n")
# file.write("css\n")

# file.close()

# import os       
# import shutil

# os.mkdir("new_folder")          #  <- Создание папки | директории 
# os.rmdir("new_folder")              # <- удаление папки

# shutil.rmtree("new_folder")       # <- удаление папки и содержимого #

    ### удалить файл ###
# os.remove("db copy.txt")
    ### переименование ###
# os.rename("new_folder", "old_folder")
# os.rename("db.txt", "db_txt_2")

    ### Создать копию файла ###
# shutil.copy("db.txt_2", "db_new_copy.txt")

    ### Создать копию папки ###
# shutil.copytree("old_folder", "new_folder_copy")


    ### пути ###
# 1) - относительный 
# file = open(r"../../../new_folder_copy/","r")
# print(file.read())
# file.close()

#2) - абсолютный 
# file = open("C:\Users\Татьяна\Desktop\python5\new_folder_copy", "r")
# print(file.read())
# file.close()

    ### Easy A ###
# try:
#     file = open("new_file.txt", "x")
# except FileExistsError:
#     print("Файл уже создан")
# else:
#     print("Файл был успешно создан")

    ### Easy B ###
# import os 
# os.remove("new_file.txt")
# print("Файл был удален")

    ### Easy C ###
# name_file = input("Введите имя файла: ")
# form_file = input("Введите формат файла: ")
# c_file = open(name_file+"."+form_file, "x")
# print(f"Файл {c_file} был успешно создан")
# c_file.close()

    ### Easy D ###
# import os
# f_file = input("введите файл для удаления: ")
# try:
#     os.remove("C:/Users/Татьяна/Desktop/python5/" + f_file)
# except FileNotFoundError:
#     print("Файл не найден")
# else:
    # print(f"Файл {f_file} был удален")

    ### Medium A ###
# import os
# file = input("Введите название файла: ")
# n_file = input("Введите новое название файла: ")
# try:
#     os.rename("C:/Users/Татьяна/Desktop/python5/" + file, n_file)
# except FileNotFoundError:
#     print("ERROR")
# else:
#     print("Done")

    ### Medium B ###
# num_of_word = int(input("Введите кол-во слов: "))
# words = input("Введите строку: ").split()[:num_of_word]
# file = open("home_text_file.txt", "a")
# for i in words:
#     file.write(f"{i}\n")
# file.close()

    ### Medium C ###
# num_of_word = int(input("Введите кол-во слов: "))
# words = input("Введите строку: ").split()[:num_of_word]
# with open('home_text_file.txt', "a") as htf:
#     for i in words:
#         htf.write(f"{i}\n")

    ### Hard A ###
# file = open("hardA.txt", "r")
# content = file.read()
# print(content.upper())

    ### Hard B ###
# import shutil
# import os
# # shutil.copy("hardB.txt", "decode.txt")
# os.remove("hardB.txt")

