    ### Easy ###
# class University:
#     def __init__(self, off_name, location):
#         self.off_name = off_name
#         self.location = location
#     def show_inf_univer(self):                          # Функция для просмотра университета #
#         print(f"Университет: {self.off_name}\nЛокация: {self.location}")
#         print()

# class Student(University):
#     def __init__(self, off_name, location, full_name, speciality):
#         super().__init__(off_name, location)
#         self.full_name = full_name
#         self.speciality = speciality
#     def show_inf_stud(self):                                             # функция для просмотра данных студента #
#         print(f"Университет: {self.off_name}\nЛокация: {self.location}\nИмя студента: {self.full_name}\nСпециальность студента: {self.speciality}")
#         print()

# class Professor(University):
#     def __init__(self, off_name, location, full_name, subject):
#         super().__init__(off_name, location)
#         self.full_name = full_name
#         self.subject = subject
#     def show_inf_proff(self):                                       # функция для просмотра данных профессора #     
#         print(f"Университет: {self.off_name}\nЛокация: {self.location}\nИмя профессора: {self.full_name}\nПредмет преподавания: {self.subject}")
#         print()

# universitet = University("МГУ", "Москва")
# student = Student("МГУ", "Москва", "Иван", "Математика")                      # <- данные для примера #
# professor = Professor("МГУ", "Москва", "Николай", "it")

# universitet.show_inf_univer()
# student.show_inf_stud()
# professor.show_inf_proff()

    ### Medium ###
# class Table:
#     def __init__(self,len_tb : int|float , wid_tb: int|float):
#         self.len_tb = len_tb
#         self.wid_tb = wid_tb
#     def square_table(self) -> float:
#         return(f"Площадь занимаемая столом: {self.len_tb * self.wid_tb * self.heig_tb} m3")

# class DeskTable(Table):
#     def __init__(self,len_tb : int|float , wid_tb: int|float, heig_tb: int|float):
#         super().__init__(len_tb, wid_tb)
#         self.heig_tb = heig_tb          # добавление высоты стола #
#     def square_table(self) -> float:
#         return(f"Площадь поверхности стола: {self.len_tb * self.wid_tb}")

# x = DeskTable(0.8, 0.6, 0.7)
# print(x.square_table())

#     ### Hard ###
# class Table:
#     def __init__(self,len_tb : int|float , wid_tb: int|float):
#         self.len_tb = len_tb
#         self.wid_tb = wid_tb
#     def square_table(self) -> float:
#         return(f"Площадь занимаемая столом: {self.len_tb * self.wid_tb * self.heig_tb} m3")

# class DeskTable(Table):
#     def __init__(self,len_tb : int|float , wid_tb: int|float, heig_tb: int|float, monit_len: int|float):
#         super().__init__(len_tb, wid_tb)
#         self.heig_tb = heig_tb              # добавление высоты стола #
#         self.monit_len = monit_len             # Добавление площади монитора # 
#     def square_table(self) -> float:
#         return(f"Площадь поверхности стола: {self.len_tb * self.wid_tb}")

# class ComputerTable(DeskTable):
#     def __init__(self, len_tb: int|float , wid_tb: int|float, heig_tb: int|float, monit_len: int|float):
#         super().__init__(len_tb, wid_tb, heig_tb, monit_len)
#     def square_table(self) -> float:
#         return (f"Площадь поверхности стола с учетом монитора: {(self.len_tb * self.wid_tb) - self.monit_len}")
    
# x = ComputerTable(0.8, 0.6, 0.7, 0.3)
# print(x.square_table())

    ### Medium ###
# class Table:
#     def __init__(self, l, w, h):
#         self.length = l
#         self.width = w
#         self.height = h

# class DeskTable(Table):
#     def get_area(self):
#         return self.length * self.width
    
# class ComputerTable(DeskTable):
#     def __init__(self, l, w, h, monitor_area):
#         super().__init__(l,w,h)
#         self.monitor_area = monitor_area
#     def get_free_area(self):
#         return super().get_area() - self.monitor_area
   
# x = ComputerTable(0.8, 0.6, 0.7, 0.3)
# print(x.get_free_area())
# print(x.get_area())


