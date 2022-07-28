# 1. Дано целое число (int). Определить сколько нулей в этом числе.

# value = 67803790097473870
# print(str(value).count('0'))

# 2. Дано целое число (int). Определить сколько нулей в конце этого числа. Например для числа 1002000 - три нуля

# value = 678037900974738700000
# value = str(value)[::-1]
# print(value, type(value))
# res= 0
# for index in value:
#     if index == '0':
#         res+=1
#     else:
#         break
# print(res)

# 3. Даны списки my_list_1 и my_list_2.
# Создать список my_result в который вначале поместить
# элементы на четных местах из my_list_1, а потом все элементы на нечетных местах из my_list_2.

# my_list1 = [4,5,6,2,3,5]
# my_list2 = [1,4,6,6,4,3]
# res=[]
# for val in my_list1[1::2]:
#         res.append(val)
# for val1 in my_list2[::2]:
#         res.append(val1)
# print(res)

# 4. Дан список my_list. СОЗДАТЬ НОВЫЙ список new_list у которого первый элемент из my_list
# стоит на последнем месте. Если my_list [1,2,3,4], то new_list [2,3,4,1]

# my_list = [4,5,6,2]
# new_list = []
# for ind in my_list[1:]:
#     new_list.append(ind)
# new_list.append(my_list[0])
# print(new_list)

# 5.Дан список my_list. В ЭТОМ списке первый элемент переставить на последнее место.
# [1,2,3,4] -> [2,3,4,1]. Пересоздавать список нельзя! (используйте метод pop)

# my_list = [5,-6,0,13]
# for ind in my_list[0:1]:
#     my_list.append(ind)
# my_list = my_list[::-1]
# my_list.pop()
# my_list = my_list[::-1]
# print(my_list)

# 6. Дана строка в которой есть числа (разделяются пробелами).
# Например "43 больше чем 34 но меньше чем 56". Найти сумму ВСЕХ ЧИСЕЛ (А НЕ ЦИФР) в этой строке.
# Для данного примера ответ - 133. (используйте split и проверку isdigit)

# mystr = "43 больше чем 34 но меньше чем 56"
# mystr = mystr.split(" ")
# mystr2 = []
# for val in mystr:
#     if val.isdigit():
#         mystr2.append(int(val))
# print(sum(mystr2))

# 7. Дана строка my_str в которой символы МОГУТ повторяться и два символа l_limit, r_limit,
# которые точно находятся в этой строке. Причем l_limit левее чем r_limit.
# В переменную sub_str поместить НАИБОЛЬШУЮ часть строки между этими символами.
# my_str = "My long string", l_limit = "o", r_limit = "g" -> sub_str = "ng strin".

# mystr = "My long string"
# l_limit = "o"
# r_limit = "g"
# substr = []
# rightlimit = False
# leftlimit = False
# for ind in mystr[::-1]:
#     if leftlimit is False:
#         if ind != l_limit:
#             if ind == r_limit:
#                  if rightlimit is True:
#                      substr.append(ind)
#                  else:
#                         rightlimit = True
#                         continue
#             else:
#                   substr.append(ind)
#         else:
#             break
#
# print("" .join(substr[::-1]))


# 8. Дана строка my_str. Разделите эту строку на пары из двух символов и поместите эти пары в список.
# Если строка содержит нечетное количество символов, пропущенный второй символ последней пары должен
# быть заменен подчеркиванием ('_'). Примеры: 'abcd' -> ['ab', 'cd'], 'abcde' -> ['ab', 'cd', e_']
# (используйте срезы длинны 2)

mystr = "ussr+"
mylist = []
for my


# 9. Дан список чисел. Определите, сколько в этом списке элементов,
# которые больше суммы двух своих соседей (слева и справа), и НАПЕЧАТАЙТЕ КОЛИЧЕСТВО таких элементов.
# Крайние элементы списка никогда не учитываются, поскольку у них недостаточно соседей.
# Для списка [2,4,1,5,3,9,0,7] ответом будет 3 потому что 4 > 2+1, 5 > 1+3, 9>3+0.
#
# mylist = [2,4,1,5,3,9,0,7]
# numbers = []
# if