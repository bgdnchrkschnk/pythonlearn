# ###################################################################
# def sort_by_bday(pers_dict):
#     age = pers_dict["age"]
#     ages = re.findall(r'[0-9]+', age)
#     if len(ages) > 1:
#         return int(ages[1])
#     else:
#         return 1000000

# def sort_by_age(pers_dict):
#     age = pers_dict["age"]
#     return age
#
# def sort_by_name(pers_dict):
#     name = pers_dict["name"]
#     return name
#
# def sort_by_name_len(pers_dict):
#     name_len = len(pers_dict["name"])
#     return name_len
#
# def sort_by_name_len_and_alphabet(pers_dict):
#     name = pers_dict["name"]
#     return len(name), name
#
#
# persons = [
#     {"name": "Jon", "age": 72},
#     {"name": "Jackhwebuffew", "age": 42},
#     {"name": "Stephany", "age": 12},
#     {"name" : "Jacob", "age": 37}
# ]
#
# new_persons = sorted(persons, key=sort_by_name_len_and_alphabet)
# print(new_persons)
#
import re
def sorted_by_bday(pers_dict):
    age = pers_dict["age"]
    ages = re.findall(r'[0-9]', age)



persons = [
    {"name": "Jon", "age": "Годы жизни: 1820 - 1887"},
    {"name": "Jackhwebuffew", "age": " 1813 -- 1854 "},
    {"name": "Stephany", "age": "1841 - 1879"},
    {"name" : "Jacob", "age": "1850 - 1896"}
]
new = sorted(persons, key=sorted_by_bday)
print(new)
