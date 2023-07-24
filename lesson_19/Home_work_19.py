    ### Easy A ###
# import re
# text = input()    
# dates = re.findall(r"[0-9]{2}-[0-9]{2}-[0-9]{4}", text)
# print(dates)

    ### Easy B ###
# import re
# text = input("Введите строку: ")
# result = re.findall(r"\b[aeiouyAEIOUY]\w*", text)
# result_2 = re.findall(r"\b[aeiouy][a-z]*\b", text, flags = re.IGNORECASE)
# print(result)
# print(result_2)

    ### Medium A ###
# import re
# text = input("Введите строку: ")
# print(bool(re.search(r"[0-9]$", text)))

    ### Medium B ###
# import re
# text = input("Введите строку: ")
# s_tx = list(text)                                 
# for i, simb in enumerate(s_tx):
#     if re.match(r"\d", simb):
#         print(f"{simb}\nИндекс: {i}")

    ### 2 - способ решения задачи ###
# import re
# text = input("Введите строку: ")
# res = re.search(r"\d+", text)
# print(res.group(0))
# print(res.span())               # интервал значения, выводится индексами #
# print(res.start())              # начальный индекс #
# print(res.end())                # конечный индекс #
    ### Hard A ###
# import re
# text = input("Введите текст: ")
# words = re.findall(r"\b\w{5}\b", text)
# print(words)

    ### Hard B ###
# kebab - case: my-first-name
# CamelCase: MyFirstName
# SnakeCase: my_first_case

# import re
# camel_case = input()
# snake_case = re.sub(r"([A-Z])", r"_\1", camel_case)[1:].lower()
# print(snake_case)