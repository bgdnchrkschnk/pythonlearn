# mydict = {"name":"Bogdan", "surname":"Cherkaschenko", "age" : 26}
# mydict["address"] = "prospkt Shevchenko"
# print(mydict)

# val = list("asd")
# digits = list("12345678")
# students = ["Cherkaschenko", "Shpanchuk", "Okhrimenko", "Murovanuy", "Urgaliev", "Dzhavahishvili"]
# print(dict(zip(digits,students)))
# print(list(zip(students,digits,val)))


# keys = ["a", "b", "c"]
# dic = {status:200 for status in keys}
# print(dic)

# table = {chr(name):name for name in range (ord("a"), ord("z") +1)}
# print(table)
# tmp_val = "f" in table
# print(tmp_val)
#
# table = {chr(name):name for name in range (ord("a"), ord("z") +1)}
# print(table)
# for val in table:
#     print(val, type(val))

# table = {chr(name):name for name in range (ord("a"), ord("z") +1)}
# for key in table:
#     print(key, table[key], type(table[key]))
# table.clear()
# print(table )


# table = {chr(name):name for name in range (ord("a"), ord("z") +1)}
# print(table.get("a", "pysto"))

# table = {chr(name):name for name in range (ord("a"), ord("z") +1)}
# # for key, val in table.items():
# #     print(key, val)
# print(table.keys())

# dict_1 = {1:11, 2:2, 3:33}
# dict_2 = {1:11, 24:22, 3:11}
#
# res = list(set(dict_1.values()).intersection(set(dict_2.values())))
# print(res)

# dict_2 = {1:11, 24:22, 3:11}
# new_dict = {value: key for key, value in dict_2.items()}
# print(new_dict)

# dict_1 = {1:11, 2:2, 3:33}
# dict_2 = {1:11, 24:22, 3:11}
# dict_1.update(dict_2)
# print(dict_1
#
# dict_1 = {1:11, 2:2, 3:33}
# dict_2 = {1:11, 24:22, 3:11}
# new_dict = {**dict_1, **dict_2}
# print(new_dict)
#
# price_list = [{"bread": 10}, {"water": 16}, {"banana": 2000}, {"water": 12}]
# min_value_list = []
# for val in price_list:
#     min_value_list.append(list(val.values())[0])
# print(min(min_value_list))
# for price in price_list:
#     if list(price.values())[0] == min(min_value_list):
#         print(list(price.keys())[0])

