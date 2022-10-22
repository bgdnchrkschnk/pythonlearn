import os

# 1. Написать функцию, которая получает в виде параметра имя файла названия интернет доменов (domains.txt)
# и возвращает их в виде списка строк (названия возвращать без точки).

# domains_path = "domains.txt"
# def my_domains(domains_path):
#     with open (domains_path, "r") as txt:
#         readlines = txt.readlines()
#     domains = []
#     for line in readlines:
#         domains.append(line[1:-1])
#     print(domains)
# my_domains(domains_path)

# 2. Написать функцию, которая получает в виде параметра имя файла (names.txt)
# и возвращает список всех фамилий из него.
# Каждая строка файла содержит номер, фамилию, страну, некоторое число (таблица взята с википедии).
# Разделитель - символ табуляции "\t"

# names_path = "names.txt"
# def get_surnames(names_path):
#     with open (names_path, "r") as txt:
#         surnames = []
#         new_surnames = []
#         readlines = txt.readlines()
#         for line in readlines:
#             surnames.append(line.split())
#         for val in surnames:
#             new_surnames.append(val[1])
#         print(new_surnames)
# get_surnames(names_path)

# # 3. Написать функцию, которая получает в виде параметра имя файла (authors.txt) и возвращает список
# # словарей вида {"date_original": date_original, "date_modified": date_modified}
# # в которых date_original - это дата из строки (если есть),
# # а date_modified - эта же дата, представленная в формате "dd/mm/yyyy" (d-день, m-месяц, y-год)
# # Например [{"date_original": "8th February 1828", "date_modified": 08/02/1828},  ...]
#
#


def take_data_date(file_name):
    with open(file_name, "r") as txt_file:
        data = txt_file.readlines()
    return data

def create_split_list(file_name):
    res = []
    for data in take_data_date(file_name):
        data = data.split("-")[0]
        data = data.split()
        if len(data) == 3:
            res.append(data)
        return res

print(create_split_list("authors.txt"))