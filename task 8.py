# 1) Дан список словарей persons в формате [{"name": "John", "age": 15}, ... ,{"name": "Jack", "age": 45}]
# а) Напечатать имя самого молодого человека. Если возраст совпадает - напечатать все имена.

# persons = [{"name": "John", "age": 15},
#            {"name": "Denis", "age": 16},
#            {"name": "Jack", "age": 45},
#            {"name": "Nikolay", "age": 13}]
# age = []
# names = []
# for pers in persons:
#     age.append(pers["age"])
#     names.append("name")
#
# age_min = min(age)
#
#
#
# # б) Напечатать самое длинное имя. Если длина имени совпадает - напечатать все имена.
#
# persons = [{"name": "John", "age": 15},
#            {"name": "Denis", "age": 15},
#            {"name": "Jack", "age": 45},
#            {"name": "Nikolay", "age": 18},
#            {"name": "Nikifor", "age": 11}]
# name = []
# for pers in persons:
#     name.append(pers["name"])
# for nam in name:
#     if len(nam) == len(max(name, key=len)):
#         print(nam)
#
# # в) Посчитать среднее количество лет всех людей из списка.
#
# persons = [{"name": "John", "age": 15},
#            {"name": "Denis", "age": 15},
#            {"name": "Jack", "age": 45},
#            {"name": "Nikolay", "age": 18},
#            {"name": "Nikifor", "age": 11}]
# ages = []
# for pers in persons:
#     ages.append(pers["age"])
# avg = (sum(ages)) / len(ages)
# print(avg)

# 2) Даны два словаря my_dict_1 и my_dict_2.
# а) Создать список из ключей, которые есть в обоих словарях.

# my_dict_1 = {"name": "John", "age": 15,
#              "city":"Washington"}
# my_dict_2 = {"name": "Boris", "age": 15,
#            "names": "Denis", "agef": 15,
#            "namec": "Jackson", "agev": 45,
#            "nameq": "Vladimir", "agee": 18,
#            "namel": "Daniil", "age1": 11,}
# print(list(set(my_dict_2.keys()).intersection(set(my_dict_1.keys()))))

# б) Создать список из ключей, которые есть в первом, но нет во втором словаре.

# my_dict_1 = {"name": "Boris", "age": 15,
#            "names": "Denis", "agef": 15,
#            "namec": "Jackson", "agev": 45,
#            "nameq": "Vladimir", "agee": 18,
#            "namel": "Daniil", "age1": 11,}
# my_dict_2 = {"name": "John", "age": 15,
#              "city":"Washington"}
# res = list(set(my_dict_1).difference(set(my_dict_2)))
# print(res)


# в) Создать новый словарь из пар {ключ:значение}, для ключей, которые есть в первом, но нет во втором словаре.

# my_dict_1 = {"name": "Boris", "age": 15,
#            "names": "Denis", "agef": 15,
#            "namec": "Jackson", "agev": 45,
#            "nameq": "Vladimir", "agee": 18,
#            "namel": "Daniil", "age1": 11,}
# my_dict_2 = {"name": "John", "age": 15,
#              "city":"Washington"}
# res = list(set(my_dict_1.keys()).difference(set(my_dict_2.keys())))
# resdict = {}
# for i in res:
#     resdict[i] = my_dict_1[i]
# print(resdict)

# г) Объединить эти два словаря в новый словарь по правилу:
# если ключ есть только в одном из двух словарей - поместить пару ключ:значениe

# my_dict_1 = {"name": "Boris", "age": 15,
#            "names": "Denis", "agef": 15,
#            "namec": "Jackson", "agev": 45,
#            "nameq": "Vladimir", "agee": 18,
#            "namel": "Daniil", "age1": 11,"city":"New York"}
# my_dict_2 = {"name": "John", "age": 15,
#              "city":"Washington"}
# res = {}
# for key in my_dict_1:
#     if key not in my_dict_2:
#         res[key] = my_dict_1[key]
# for key in my_dict_2:
#     if key not in my_dict_1:
#         res[key] = my_dict_2[key]
# print(res)

###################
# res1 = list(set(my_dict_1.keys()).difference(set(my_dict_2.keys())))
# res2 = list(set(my_dict_2.keys()).difference(set(my_dict_1.keys())))
# res = {}
# for i in res1:
#     res[i] = my_dict_1[i]
# for i in res2:
#     res[i] = my_dict_2[i]
# print(res)
# если ключ есть в двух словарях - поместить пару {ключ: [значение_из_первого_словаря, значение_из_второго_словаря]},

my_dict_1 = {"name": "Boris", "age": 15,
           "names": "Denis", "agef": 15,
           "namec": "Jackson", "agev": 45,
           "nameq": "Vladimir", "agee": 18,
           "namel": "Daniil", "age1": 11,"city":"New York"}
my_dict_2 = {"name": "John", "age": 16,
             "city":"Washington"}
res = {}
for key in my_dict_1:
    if key in my_dict_2:
        res[key] = [my_dict_1[key], my_dict_2[key]]
print(res)