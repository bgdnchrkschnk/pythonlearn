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

data = [{"name": "John", "age": 15},
           {"name": "Denis", "age": 16},
           {"name": "Jack", "age": 45},
           {"name": "Nikolay", "age": 13},
        {"name": "Oleksander", "age": 26}]

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

res = lambda x, y, z=3: x + y + z
result = res(5,6)
print(result)