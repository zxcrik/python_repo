    ### Easy ###
# def h_file(check_file: str) -> str:
#     while True:
#         try:
#             file = open(check_file,"r")
#             break
#         except FileNotFoundError:
#             print("Файл не найден!")
#             check_file = input("Введите правильное название файла: ")
#     line = int(input(f"Введите кол-во строк для печати из файла {check_file}: "))
#     for i in range(line):
#         print(*file.readlines(line), end = '')
#     file.close()
# check_file = input("Введите файл для проверки: ")
# h_file(check_file)

    ### Medium ###
# try:
#     with  open("ethics.txt", "r")  as e_file:
#         lines = e_file.readlines()

#         print("Нечетные строки: ")
#         for i in range(0,len(lines),2):
#             print(lines[i].strip())

#         print("Четные строки: ")
#         for j in range(1,len(lines), 2):
#             print(lines[j].strip())
# except FileNotFoundError:
#     print("Файл не найден!")

     ### 2 - вариант решения задачи ###
# file = open("ethics.txt", "r")
# lines = file.readlines()
# print("Нечетные")
# print()

    ### Hard ###
# import os
# import shutil
# n_file = open("new_ethics.txt", "x")               # 1  и  2 #
# eth_file = open("ethics.txt", "r")
# for i in range(6):                            
#     file_r = eth_file.readline()
#     n_file.write(file_r)
# n_file.close()
# eth_file.close() 

# for i in range(1,4):                                           
#     shutil.copy("new_ethics.txt", f"new_ethics_copy_{i}.txt")       # 3 #

# for j in range(1,4):
#     os.mkdir(f"new_ethics_pap_{j}")        # 4 #

# for k in range(1,4):
#     shutil.move(f"new_ethics_copy_{k}.txt", f"new_ethics_pap_{k}")   # 5 #

# os.remove("new_ethics.txt")            # 6 #
