# # ###################################################################
# # def sort_by_bday(pers_dict):
# #     age = pers_dict["age"]
# #     ages = re.findall(r'[0-9]+', age)
# #     if len(ages) > 1:
# #         return int(ages[1])
# #     else:
# #         return 1000000
#
# # def sort_by_age(pers_dict):
# #     age = pers_dict["age"]
# #     return age
# #
# # def sort_by_name(pers_dict):
# #     name = pers_dict["name"]
# #     return name
# #
# # def sort_by_name_len(pers_dict):
# #     name_len = len(pers_dict["name"])
# #     return name_len
# #
# # def sort_by_name_len_and_alphabet(pers_dict):
# #     name = pers_dict["name"]
# #     return len(name), name
# #
# #
# # persons = [
# #     {"name": "Jon", "age": 72},
# #     {"name": "Jackhwebuffew", "age": 42},
# #     {"name": "Stephany", "age": 12},
# #     {"name" : "Jacob", "age": 37}
# # ]
# #
# # new_persons = sorted(persons, key=sort_by_name_len_and_alphabet)
# # print(new_persons)
# #
# # import re
# # def sorted_by_bday(pers_dict):
# #     age = pers_dict["age"]
# #     ages = re.findall(r'[0-9]+', age)
# #     return int(ages[0])
# #
# #
# #
# # persons = [
# #     {"name": "Jon", "age": "Годы жизни: 1820 - 1887"},
# #     {"name": "Jackhwebuffew", "age": " 1813 -- 1854 "},
# #     {"name": "Stephany", "age": "1841 - 1879"},
# #     {"name" : "Jacob", "age": "1850 - 1896"}
# # ]
# # new = sorted(persons, key=sorted_by_bday)
# # print(new)
#
# import random
# import string
# def generate_string(min, max):
#     str_list = [random.choice(string.ascii_lowercase) for _ in range(random.randint(min,max))]
#     return "" .join(str_list)
#
# def create_spaces(some_str):
#     some_str_list = list(some_str)
#     space_number = 0
#     while space_number < len(some_str):
#         new_space = random.randint(1,8)
#         space_number += new_space
#         some_str_list[new_space] = " "
#     return "" .join(some_str_list)
#
# def transform_string(some_str):
#     spaced_string = create_spaces(some_str)
#     return some_str
#
# my_string = generate_string(30,50)
# new_str = transform_string(my_string)
# print(my_string)

# import re
# str = "AC/DCAC/DCAC/DCAC/DCAC/DCAC/DCAC/DCAC/DCAC/DCAC/DCAC/DC"
#
# result = re.fullmatch('AC/DCAC/DCAC/DCAC/DCAC/DCAC/DCAC/DCAC/DCAC/DCAC/DCAC/DC', str)
# print(result)
