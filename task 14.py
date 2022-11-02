# Все пункты сделать как отдельные функции(можно создавать дополнительные вспомагательные функции)
#
# 1. Написать функцию, которая получает в виде параметра имя файла названия интернет доменов (domains.txt)
# и возвращает их в виде списка строк (названия возвращать без точки).
#
# 2. Написать функцию, которая получает в виде параметра имя файла (names.txt)
# и возвращает список всех фамилий из него.
# Каждая строка файла содержит номер, фамилию, страну, некоторое число (таблица взята с википедии).
# Разделитель - символ табуляции "\t"
#
# 3. Написать функцию, которая получает в виде параметра имя файла (authors.txt) и возвращает список
# словарей вида {"date_original": date_original, "date_modified": date_modified}
# в которых date_original - это дата из строки (если есть),
# а date_modified - эта же дата, представленная в формате "dd/mm/yyyy" (d-день, m-месяц, y-год)
# Например [{"date_original": "8th February 1828", "date_modified": 08/02/1828},  ...]

# class AutoGet:
#     def __init__(self, domains_path, names_path):
#         self.domains_path = domains_path
#         self.names_path = names_path
#         self.my_domains()
#         self.get_surnames()
#
#     def my_domains(self):
#         with open (self.domains_path, "r") as txt:
#             readlines = txt.readlines()
#         domains = []
#         for line in readlines:
#             domains.append(line[1:-1])
#         print(domains)
#
#     def get_surnames(self):
#         with open (self.names_path, "r") as txt:
#             surnames = []
#             new_surnames = []
#             readlines = txt.readlines()
#             for line in readlines:
#                 surnames.append(line.split())
#             for val in surnames:
#                 new_surnames.append(val[1])
#             print(new_surnames)
#
# num1 = AutoGet("domains.txt", "names.txt")
