# # обработка исключений
# from random import randint
# value = randint(1, 10)
# var_value = input("Угадай число от 1 до 10:")
# try: - если введённые данные можно привести к типу int то выполнять дальше
#    var_value = int(var_value)
#    while var_value != value:
#        if var_value > value:
#            var_value = int(input("Попробуй меньше!"))
#        elif var_value < value:
#            var_value = int(input("Попробуй больше!"))
#            print("Правильно!")
#    else:
#        print("Правильно!")
# except ValueError: - если нет - то выполняем это
#    print("Failed")


# val1 = ord('b')
# print (val1)
# val2 = chr(33)
# print(val2)


# list1 = [-2, -16, 3, 0, 96]
# list1.sort()
# print(list1)

# list1 = [-2, -16, 3, 0, -96]
# list2 = sorted(list1, reverse=True)
# print(list2)

# list1 = list("qwVUYtftyuiyodw2")
# list1.sort(reverse=True)
# print(list1)

# value1 = "blablacar"
# value2 = "bla"
# res = value1.count(value2)
# for valv in [value2] * res:
#     print(valv)

# val1 = 'bla'
# res = [val1] * 3
# for valv in res:
#     print(valv)
# print(res)

# value1 = "blablacar"
# value2 = "bla"
# count = value1.count(value2)
# for valv in range(count):
#     print("bla")


# my_str = "BLA bla car"
# res = []
# for sym in my_str.upper():
#     if sym not in res:
#         res.append(sym)
# print(len(res))


# my_str = "uhuhlauiceijihuvyw"
# my_list = []
# for sym in my_str[::2]:
#     my_list.append(sym)
# print(my_list)

# value= 'Vladimir Zelensky'
# res = 'The president of Ukraine is '
# value += res
# print(res)

# my_list = []
# my_str = "qwerty"
# str_index = [1,4,2,0,4,5,3,2,0]
# for indx in str_index:
#     my_list.append(my_str[indx])
# print(my_list)

# numb = 26756753655426326576883792
# print (int(str(numb)[::-1]), type(numb))

# numb = 26756753655426326576883792
# numb = int("" .join(sorted(str(numb))))
# print(numb, type(numb))

# numb = 26756753655426326576883792
# numb = int("" .join(sorted(str(numb), reverse=True)))
# print(numb, type(numb))
