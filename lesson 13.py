# ### ZIP function
#
# months = ["Jan", "Feb", "Mar"]
# numb = ["01", "02", "03"]
# numbs2 = (2,3,4)
#
# res = zip(numb, months, numbs2)
# # #
# print(dict(res))
# print(tuple(res))
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


# data_nech = list(filter(lambda x: x % 2, data))
# print(data_nech)
#
# my_list = [0,1,2,-3,-5,6,7,-12]
#
# res = list(filter(lambda x: len(str(abs(x))) > 1, my_list))
# print(res)
#
# data = [1,-25,16,-8,9]
# res = list(filter(lambda x: x!=abs(x), data))
# print(res)
#
# data = [1,-25,16,-8,9]
# res = list(filter(lambda x: len(str(abs(x))) > 1, data))
# print(res)


# data = ["1", "25", "- 16", "8", "9"]
# # res = []
# # [res.append(int(i)) for i in data]
# # print(res)
# res = list(map(lambda x: int(x), data))
# print(res)
#
#
# data = [1,25,16,8,9]
# res = []
# [res.append(i ** 0.5) for i in data]
# print(res)
# res = list(map(lambda x: x ** 0.5, data))
# print(res)

# data = [1,25,16,8,9]
# res = list(map(lambda x: x ** 2, data))
# print(res)
# res = [(i ** 2) for i in data ]
# print(res)

# data = [1,25,16,-8,9]
# # res = list(map(lambda x: -x, data))
# # print(res)
# res = [-i for i in data]
# print(res)

# data = [1,25,16,8,-9]
# def my_function(x):
#     if x != abs(x):
#         return -1
#     else:
#         return x ** 0.5
# res = list(map(my_function, data))
# print(res)

import requests
# link = "https://icanhazip.com/"
# link2 = "https://google.com.ua/"
# print(requests.get(link).status_code)
# print(requests.get(link ).text)

# url = "http://api.forismatic.com/api/1.0/"
# param = {"method": 'getQuote',
#          "format": "json",
#          "lang": "en",
#          "key" : 10}
#
# res_status_code = requests.get(url, params=param).status_code
# res_response = requests.get(url, params=param).text
# print(res_status_code)
# print(res_response)


import requests
def get_quotes():
    param = {"method": 'getQuote',
    "format": "json",
    "lang": "en",
    "key": 100}
    request = requests.get("http://api.forismatic.com/api/1.0/", params=param)
    data = request.json
    author = data["quoteAuthor"]
    quote = data["quoteText"]
    print(f"{author}: {quote}- (c) parser by MILAN STAR")

get_quotes()

# import requests
# headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36",
#            "Authorization" : "Bearer 4ecc7a7f15532f24821f31d2604d0bc69c19562496286a142c554e4f914c2bfb"}
# data = {"custname": "Bodik",
#         "custtel": "0966410575",
#         "custemail": "bgdnchrkschnk@gmail.com",
#         "comments": "Please call me!",
#         "size": "large",
#         "topping": "bacon",
#         "topping": "onion",
#         "topping": "mushrooms"
#         }
# request = requests.post("http://httpbin.org/post", data=data, headers=headers)
# print(request.text)