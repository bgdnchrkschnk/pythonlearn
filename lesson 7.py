# Даны списки my_list_1 и my_list_2.
# Создать список my_result в который поместить элементы из my_list_1 и
# my_list_2 через один, начиная с my_list_1.
# a) кол-во эл-тов одинаковое
#
# mylist1 = [1,3,5]
# mylist2 = [20,30,40]
# res = []
# for index in range(len(mylist1)):
#     res.append(mylist1[index])
#     res.append(mylist2[index])
# print(res)
#
# б) кол-во эл-тов разное. Оставшиеся дописать в конец.
#
# mylist1 = [1,3]
# mylist2 = [20,30,40,50,60]
# res = []
# lenn = min(len(mylist1), len(mylist2))
#
# for index in range(lenn):
#     res.append(mylist1[index])
#     res.append(mylist2[index])
#
# if len(mylist1) > len(mylist2):
#     tail = mylist1[lenn:]
# else:
#     tail = mylist2[lenn:]
#
# res += tail
# print(res)

# mylist = []
# for number in range(15):
#     mylist.append(number ** 2)
# print(mylist)

# краткая запись

# mylist = [number**2 for number in range(15)]
# print(mylist)

# mylist = [number/2 for number in range(10)[::-1]]
# mylist2 = [str(number*2) for number in range(20)[::-1]]
# print(int("" .join(mylist2)))
#
# alphabet = [chr(index) for index in range(ord("A"), ord("Z") +1)]
# print(alphabet)

# mylist = ["qwe", "asdf", "123" , 23, -16]
# newlist = [value * 2 for value in mylist if type(value) == str and len(value) > 3]
# print(newlist)

#
# mylist = ["/home/res/PycharmProjects/Pandas",
#           "/home/res/PycharmProjects/Pandas",
#           "/home/res/PycharmProjects/Pandas",
#           "/home/res/PycharmProjects/Pandas",
#           "/home/res/PycharmProjects/Pandas",
#           "/home/res/PycharmProjects/Pandas",
#           "/home/res/PycharmProjects/Pandas"]
#
# for value in mylist:
#     print(value)
#
# [print(value) for value in mylist]

# set (множества)
# mylist = ["/home/res/PycharmProjects/Pandas",
#           "/home/res/PycharmProjects/Pandas",
#           "/home/res/PycharmProjects/Pandas",
#           "/home/res/PycharmProjects/Pandas",
#           "/home/res/PycharmProjects/Hillel",
#           "/home/res/PycharmProjec ts/Pandas",
#           "/home/res/PycharmProjects/Pandas"]
#
# myset = set(mylist)
# print(myset, type(myset))


# mylist = "/home/res/PycharmProjects/Pandas"
# print(len(set(mylist)))

# mylist1 = [1,3,5,7,9,9,3]
# mylist2 = [1,3,5,7,9,9,3,3,9,9,9,9]
# print("success") if set(mylist1) == set(mylist2) else print("fail")
#
# mylist1 = [1,3,5,7,9,9,3]
# mylist2 = [1,3,5,7,9,9,3,3,9,9,9,9]
# print("success") if 7 in set(mylist1) else print("fail")


# mylist1 = "/home/res/PycharmProjects/Pandas"
# mylist2 = "/home/res/PycharmProjects/Hillel"
#
# mylist1set = set(mylist1)
# mylist2set = set(mylist2)
#
# print(mylist1set.union(mylist2set))

# mylist1 = "/home/res/PycharmProjects/Pandas"
# mylist2 = "/home/res/PycharmProjects/Hillel"
# print((set(mylist1).intersection(set(mylist2))))
#
# mylist1 = "/home/res/PycharmProjects/Pandas"
# mylist2 = "/home/res/PycharmProjects/Hillel#"
# print((set(mylist1).difference(set(mylist2))))

# mylist1 = ["asd", "rd", "d", "d", "d", "d", "d"]
# for val in set(mylist1):
#     count = mylist1.count(val)
#     print(val, count)


# person = {"name": "John",
#           "age": 23,
#           "job": ["cop", "doctor"],
#           "address": {"city": "Dnipro",
#                       "street": "Polya"}}
#
# print(person["address"]["city"])
# print(person["job"])

# key = "NEW"
# value = [1,2,3]
# dummy = {key: value}
# print(dummy)
# dummy["NEW"] = "Hello"
# print(dummy)
