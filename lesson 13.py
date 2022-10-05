# ### ZIP function
#
# months = ["Jan", "Feb", "Mar"]
# numb = ["01", "02", "03"]
# numbs2 = (2,3,4)
#
# res = zip(numb, months, numbs2)
# #
# # print(dict(res))
# # print(tuple(res))
# print(list(res))

# data = ["John", "Jim", "Jacob", "Denis", "Avanesyants"]
# data_sorted = sorted(data)
# print(data_sorted)

# data = ["John", "Jim", "Jacob", "Denis", "Avanesyants"]
# data_sorted = sorted(data, key=)
# print(data_sorted)

# lambda аргументы: выражение
#
# Тип: <class 'function'>

# data = [{"name": "John", "age": 15},
#            {"name": "Denis", "age": 16},
#            {"name": "Jack", "age": 45},
#            {"name": "Nikolay", "age": 13},
#         {"name": "Oleksander", "age": 26}]

###  Сортировка через созданную функцию

# def sort_by_age(dict):
#     data = dict.get("age")
#     return data
#
# data_sorted = sorted(data, key=sort_by_age)
# print(data_sorted)
#
# ### Сортировка через lambda
#
# data_sorted = sorted(data, key=lambda x: x["age"])
# print(data_sorted)
#
# data_sorted = sorted(data, key=lambda x: len(x["name"]), reverse=True)
# print(data_sorted)

# res = (lambda x: x+3)(2)
# print(res)
#
# res = lambda x, y: x + y
# print(res(5,6))
#
# res = lambda x, y: x + y
# result = res(5,6)
# print(result)
#
# res = lambda x, y, z: x + y + z
# print(res(5,6))

# res = lambda x, y, z=3: x + y + z
# result = res(5,6)
# print(result)

# ### Задан список словарей
# data = [{"name": "Daniel Bernoulli", "years": "1700 – 1782"},
#    {"name": "Rene Descartes", "years": "1596 – 1650"},
#    {"name": "Leonhard Euler", "years": "1707 – 1783"} ]
# ### Отсортировать заданный список по дате рождения
# import re
# def data_sorted(dict):
#     y = dict["years"]
#     x = (re.split(" ", y)[0])
#     return int(x)
#
# print(sorted(data, key=data_sorted))
#
# #
# data_sorted = sorted(data, key= lambda x: int(re.split(" ", x["years"])[0]), reverse=False)
# print(data_sorted)


# ### Задан список словарей
# data = [{"name": "Archimedes", "years": "287 BC – 212 BC"},
#     {"name": "Daniel Bernoulli", "years": "1700 – 1782"},
#    {"name": "Rene Descartes", "years": "1596 – 1650"},
#    {"name": "Euclid", "years": "325 BC – 270 BC"},
#    {"name": "Leonhard Euler", "years": "1707 – 1783"} ]
# ### Отсортировать заданный список по дате рождения
#
# import re
# def data_sorted(dict):
#     y = dict["years"]
#     if len((y.split(" "))[0]) > 3:
#         x = int((y.split(" "))[0])
#     else:
#         x = int("-1" + (y.split(" "))[0])
#     return x
# print(data_sorted(data[0]))
# print(sorted(data, key=data_sorted))
# #
# #
# data_sorted = sorted(data, key= lambda x: int((x["years"].split(" "))[0]) if len((x["years"].split(" "))[0]) > 3 else int("-1" + (x["years"].split(" "))[0]))
# print(data_sorted)


### Задан список
data = [ 1, 23, 12, 90, 45]
### Создать список, включающий только нечетные числа из этого списка
# res = []
# [res.append(x) for x in data if x%2]
# print(res)


data_nech = list(filter(lambda x: x % 2, data))
print(data_nech)