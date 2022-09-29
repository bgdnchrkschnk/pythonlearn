# # Для задания 1-7 за основу можете взять код из ДЗ № 7.
# #
# # 1. Написать функцию которой передается один параметр - список строк my_list.
# # Функция возвращает новый список в котором содержаться
# # элементы из my_list по следующему правилу:
# # Если строка стоит на нечетном месте в my_list, то ее заменить на
# # перевернутую строку. "qwe" на "ewq".
# # Если на четном - оставить без изменения.
#
#
# # mylist = ["Bogdan", "Denys", "Illya", "Maksym", "Vladislav", "Argam"]
# # new_list = []
# # def new(mylist):
# #     for index, value in enumerate(mylist):
# #         if not index % 2:
# #             new_list.append(value[::-1])
# #         else:
# #             new_list.append(value)
# #     print(new_list)
# # new(mylist)
#
#
# # 2. Написать функцию которой передается один параметр - список строк my_list.
# # Функция возвращает новый список в котором содержаться
# # элементы из my_list у которых первый символ - буква "a".
#
#
# # mylist = ["Bogdan", "Denys", "Illya", "Maksym", "Vladislav", "Argam"]
# # new_list = []
# # def new(mylist):
# #     for value in mylist:
# #         if value[0] == "A":
# #             new_list.append(value)
# #         else:
# #             continue
# #     print(new_list)
# # new(mylist)
#
#
# # 3. Написать функцию которой передается один параметр - список строк my_list.
# # Функция возвращает новый список в котором содержаться
# # элементы из my_list в которых есть символ - буква "a" на любом месте.
#
#
# # mylist = ["Bogdan", "Denys", "Illya", "Maksym", "Vladislav", "Argam"]
# # new_list = []
# # def new(mylist):
# #     for value in mylist:
# #         if "a" in value or "A" in value:
# #             new_list.append(value)
# #     print(new_list)
# # new(mylist)
#
#
# # 4. Написать функцию которой передается один параметр - список строк my_list в
# # котором могут быть как строки (type str) так и целые числа (type int).
# # Функция возвращает новый список в котором содержаться только строки из my_list.
#
# # mylist = ["Bogdan", "Denys", 15, 18, "Illya", -2, "Maksym", -18, "Vladislav", "Argam", "-999"]
# # new_list = []
# # def new(mylist):
# #     for value in mylist:
# #         if type(value) == str:
# #             new_list.append(value)
# #     print(new_list)
# # new(mylist)
#
# # 5. Написать функцию которой передается один параметр - строка my_str.
# # Функция возвращает новый список в котором содержаться те символы из my_str,
# # которые встречаются в строке только один раз.
#
# # my_str = "Hello, my name is Bogdanchik!"
# # new_list = []
# # def new(my_str):
# #     for value in my_str:
# #         for val in value:
# #             if my_str.count(val) == 1:
# #                 new_list.append(val)
# #     print(new_list)
# # new(my_str)
#
# # 6. Написать функцию которой передается два параметра - две строки.
# # Функция возвращает список в который поместить те символы,
# # которые есть в обеих строках хотя бы раз.
#
# # mystr1 = "Kyiv is a capital of Ukrane"
# # mystr2 = "London is a capital of Great Britane"
# # def symbols_intersection(mystr1, mystr2):
# #     res = list(set(mystr1).intersection(set(mystr2)))
# #     return res
# # print(symbols_intersection(mystr1, mystr2))
#
# # 7. Написать функцию которой передается два параметра - две строки.
# # Функция возвращает список в который поместить те символы, которые есть в обеих строках,
# # но в каждой только по одному разу.
#
# # mystr1 = "Kyiv is a capital of Ukrane"
# # mystr2 = "London is a capital of Great Britane"
# # res = []
# # def new(mystr1, mystr2):
# #     for value in mystr1:
# #         if mystr1.count(value) == 1 and mystr2.count(value) == 1:
# #             res.append(value)
# #     return res
# # print(new(mystr1, mystr2))
#
#
# # 8. Даны списки names и domains (создать самостоятельно).
# # Написать функцию для генерирования e-mail в формате:
# # фамилия.число_от_100_до_999@строка_букв_длинной_от_5_до_7_символов.домен
# # фамилию и домен брать случайным образом из заданных списков переданных в функцию в виде параметров.
# # Строку и число генерировать случайным образом.
# #
# # Пример использования функции:
# # names = ["king", "miller", "kean"]
# # domains = ["net", "com", "ua"]
# # e_mail = create_email(domains, names)
# # print(e_mail)
# # >>>miller.249@sgdyyur.com

import random
import string
names = ["Bogdan", "Dmitry", "Vladislav", "Andriy", "Sergiy"]
domains = ["com", "net", "ua", "od.ua", "ru"]
def create_emails(names, domains):
    text = [random.choice(string.ascii_lowercase) for _ in range(random.randint(5,7))]
    text = ''.join(text)
    email = f"{random.choice(names)}.{random.randint(100,1000)}@{text}.{random.choice(domains)}"
    return email
print(create_emails(names, domains))