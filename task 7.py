# 1. Дан список строк my_list. Создать новый список в который поместить
# элементы из my_list по следующему правилу:
# Если строка стоит на нечетном месте в my_list, то ее заменить на
# перевернутую строку. "qwe" на "ewq".
# Если на четном - оставить без изменения.
# Задание сделать с использованием enumerate или range.

# mylist = ["Bogdan", "Denys", "Illya", "Maksym", "Vladislav", "Argam"]
# new_list = []
# for index, value in enumerate(mylist):
#     if not index % 2:
#         new_list.append(value[::-1])
#     else:
#         new_list.append(value)
# print(new_list)

# 2. Дан список строк my_list. Создать новый список в который поместить
# элементы из my_list у которых первый символ - буква "A".

# mylist = ["Bogdan", "Denys", "Illya", "Maksym", "Vladislav", "Argam"]
# new_list = []
# for value in mylist:
#     if value[0] == "A":
#         new_list.append(value)
#     else:
#         continue
# print(new_list)


# 3. Дан список строк my_list. Создать новый список в который поместить
# элементы из my_list в которых есть символ - буква "a" на любом месте.

# mylist = ["Bogdan", "Denys", "Illya", "Maksym", "Vladislav", "Argam"]
# new_list = []
# for value in mylist:
#     if "a" in value or "A" in value:
#         new_list.append(value)
# print(new_list)

# 4. Дан список my_list в котором могут быть как строки (type str) так и целые числа (type int).
# Создать новый список в который поместить только строки из my_list.

# mylist = ["Bogdan", "Denys", 15, 18, "Illya", -2, "Maksym", -18, "Vladislav", "Argam", "-999"]
# new_list = []
# for value in mylist:
#     if type(value) == str:
#         new_list.append(value)
# print(new_list)

# 5. Дана строка my_str. Создать список в который поместить те символы из my_str,
# которые встречаются в строке только один раз.
# import string
#
# my_str = "Hello, my name is Bogdanchik!"
# new_list = []
# for i in set(my_str):
#     if my_str.count(i) == 1 and i in string.ascii_letters:
#         new_list.append(i)
# print(new_list)

# 6. Даны две строки. Создать список в который поместить те символы,
# которые есть в обеих строках хотя бы раз.

# mystr1 = "Kyiv is a capital of Ukrane"
# mystr2 = "London is a capital of Great Britane"
# res = list(set(mystr1).intersection(set(mystr2)))
# print(res)

# 7. Даны две строки. Создать список в который поместить те символы, которые есть в обеих строках,
# но в каждой только по одному разу.
#
mystr1 = "Kyiv is a capital of Ukrane"
mystr2 = "London is a capital of Great Britane"
res = []
for value in set(mystr1).intersection(set(mystr2)):
    if mystr1.count(value) == 1:
        res.append(value)
print(res)


### Ещё одно решение

# mystr1 = "Kyiv is a capital of Ukrane"
# mystr2 = "London is a capital of Great Britane"
# res = []
# for i in set(mystr1):
#     if mystr1.count(i) ==1 and mystr2.count(i) == 1:
#         res.append(i)
# print(res)
# 8. Описать с помощью словаря следующую структуру для конкретного человека (можно придумать):
# Фамилия
# Имя
# Возраст
# Проживание
#     Страна
#     Город
#     Улица
# Работа
#     Наличие
#     Должность

# struc = {"Last name": "Cherkashchenko",
#          "Name": "Bogdan",
#          "Age": 26,
#          "From": {"Country": "Ukraine", "City": "Odesa", "Street": "Prospekt Shevchenko 8/10"},
#          "Job" : {"Currently": "+", "Function": "QA Engineer"}}
# print(struc["Last name"], struc["Name"], "-", struc["Job"]["Function"])


# 9. Описать с помощью словаря следующую структуру (рецепт ненастоящего торта,
# придумать и указать граммы для продуктов):
# Составляющие
#     Коржи
#         Мука
#         Молоко
#         Масло
#         Яйцо
#     Крем
#         Сахар
#         Масло
#         Ваниль
#         Сметана
#     Глазурь
#         Какао
#         Сахар
#         Масло

# struc = {"korj": {"muka": 250, "milk": 1000, "butter": 100, "eggs": 2},
#          "cream": {"sugar":75,"butter": 50, "vanilla": 25, "sour cream": 100},
#          "glasoure": {"cacao": 200, "sugar": 75, "butter": 50}}
# print(type(struc), struc)