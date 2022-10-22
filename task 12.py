# data.json - файл с данными о некоторых математиках прошлого.
# 1. Необходимо написать функцию, которая считает эти данные из файла. Параметр функции - имя файла.
import json
import re
# def read_json(path):
    # with open(path, "r") as json_file:
    #     data = json.load(json_file)
    # return data

# print(read_json("data.json"))

### ИЛИ ТАКОЙ ВАРИАНТ

def read_json(path):
    json_file = open(path)
    json_file = json.load(json_file)
    return json_file

json_file = read_json("data.json")
print(json_file)
# 2. Написать функцию сортировки данных по ФАМИЛИИ в поле "name" (у тех у кого она есть).
# Например для Rene Descartes фамилия это Descartes, у Pierre de Fermat - Fermat и т.д.
# Если фамилии нет, то использовать имя, например Euclid.

# def last_names(dict):
#     name = dict["name"]
#     res = re.split(" ", name)
#     return len(res)
#
#
# def sorted_by_lastnames(json_file):
#     new_data = sorted(json_file, key=last_names, reverse=True)
#     return new_data
#
# print(sorted_by_lastnames(json_file))
# 3. Написать функцию сортировки по дате смерти из поля "years".
# Обратите внимание на сокращение BC. - это означает до н.э.

# 4. Написать функцию сортировки по количеству слов в поле "text"

def len_words(dict):
    text = dict["text"]
    res = re.split(" ", text)
    return len(res)


def sort_by_text(json_file):
    new_data = sorted(json_file, key=len_words)
    return new_data

print(sort_by_text(json_file))
