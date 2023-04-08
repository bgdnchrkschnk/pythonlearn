# import string
# listf = [val for val in range(100) if val%2 != 0]
# print(listf)


# file = open("names.txt", "w")
# file = (file.write("Тестирую функцию записи в файл\nВроде всё ок!"))
# file_new = file
# with open ("names.txt", "r") as txt:
#     print(txt.read())

# def capitalize(a):
#     re = a.split(" ")
#     res = ""
#     for i in re:
#         res += str.title(i) + " "
#     print(res)
# capitalize("de noche todos los gatos son pardos")

# def chetka(a: int):
#     if a % 2:
#         print("nechetnoe!")
#     else:
#         print("chetnoe")
#
# chetka(32)
#
# a = int(input())
# print(f"The next number for the number {a} is {a+1}")
# print(f"The previous number for the number {a} is {a-1}.")
#
# print(sign(5))


# breakout = False
#
# for i in range(10):
#     if i == 6:
#         breakout = True
#     if breakout:
#         break
#     else:
#         print(i)


# counter = 0
# while counter < 100:
#     counter += 1
#     if counter % 2:
#         print(counter, "NECHETNOE")


# a = int(input())
# print("The next number for the number", a, "is", a+1)
# print("The previous number for the number", a, "is", a-1)


# a = int(input())
# if not a % 4 and a % 100:
#     print("YES")
# else:
#     print("NO")

## Ход короля
# a1 = int(input())
# a2 = int(input())
# b1 = int(input())
# b2 = int(input())
#
# if abs(a1) - abs(b1) <= 1 and abs(a2) - abs(b2) <= 1:
#         print("YES")
# else:
#     print("NO")



# ## Ход ладьи
# a1 = int(input())
# a2 = int(input())
# b1 = int(input())
# b2 = int(input())
#
# if a1 == b1 or a2 == b2:
#         print("YES")
# else:
#     print("NO")


# str = '''
# Hello my beauty!
# '''
# print(str)

#s1 = 'a'
# s2 = 'z'
# print(s1 < s1)

# s = "Hello"
# p = "World"
# print(s)
# breakpoint()
# print(p)

# a = int(input())
# b = int(input())
# n = int(input())
# res = (a*100+b)*n
# an = res // 100
# bn = res % 100
# print(an,bn)

# h1, m1, s1, h2, m2, s2 = [int(input()) for i in range(6)]
#
# res1 = h1*3600 + m1*60 +s1
# res2 = h2*3600 + m2*60 +s2
# res = res2 - res1
# print(res)
from math import ceil

# from math import sqrt
# a = int(input())
# b = int(input())
# x = sqrt((a ** 2) + (b ** 2))
# print(x)


# p = int(input())
# h = int(input())
# c = int(input())
# summ = h * 100 + c
# proc = summ * p
# res = proc + summ
# print(res//100, res%100)



# x = float(input())
# if x % 2:
#     print("ne4etnoe!")
# else:
#     print("4etnoe!")

# n = int(input())
# res = 0
# for i in range(n):
#     if not int(input()):
#         res+=1
# else:
#     print(res)


# n = int(input())
# sum = ""
# for i in range(1, n+1):
#     sum += str(i)
#     print(sum)

# n = int(input())
# sum =
# for i in range(n):
#     sum += i
# import math
# print(math.ceil(11/2))


# Дана строка. Найдите в этой строке второе вхождение буквы f,
# и выведите индекс этого вхождения.
# Если буква f в данной строке встречается только один раз,
# выведите число -1, а если не встречается ни разу, выведите число -2.

# s = input()
# if s.count("f") > 1:
#     a = s.find("f")
#     print(s.find("f", a+1))
# elif s.count("f") == 1:
#     print(-1)
# else:
#     print(-2)

# Условие
# Дана строка, в которой буква h встречается минимум два раза.
# Удалите из этой строки первое и последнее вхождение буквы h,
# а также все символы, находящиеся между ними.

# s = input()
# left = s.find("h")
# right = s.rfind("h") + 1
# print(s[:left]+s[right:])
# In tobbit

# Условие
# Дана строка, в которой буква h встречается как минимум два раза.
# Разверните последовательность символов,
# заключенную между первым и последним появлением буквы h, в противоположном порядке.

# s = input()
# left = s.find("h")
# right = s.rfind("h") + 1
# center = s[left:right]
# print(s[:left]+center[::-1]+s[right:])

# Условие
# Дана строка. Замените в этой строке все цифры 1 на слово one.

# s = input()
# print(s.replace("1", "one"))

# Условие
# Дана строка. Удалите из этой строки все символы @.

# s = input()
# print(s.replace("@", ""))

# Условие
# Дана строка. Замените в этой строке все появления буквы h на букву H,
# кроме первого и последнего вхождения.

# s = input()
# left = s.find("h")
# right = s.rfind("h")
# print(s[:left+1] + s[left+1:right].replace("h", "H") + s[right:])

# Условие
# Дана строка. Удалите из нее все символы, чьи индексы делятся на 3.

# s = input()
# res = ""
# for i,x in enumerate(s):
#     if not i % 3:
#         continue
#     else:
#         res+=x
# else:
#     print(res)

# ИЛИ

# s = input()
# res = ""
# for i in range(len(s)):
#     if not i % 3:
#         continue
#     else:
#         res+=s[i]
# else:
#     print(res)

# n = int(input())
# fac = 0
# for i in range(n+1):
#     fac += i
# sum = 0
# for x in range(n-1):
#     sum += int(input())
# else:
#     print(fac-sum)


# index = 0
# while index < 10:
#     print(index)
#     index += 1

# s = [1,2,3,4,5,6,4]
# while 4 in s:
#     s.remove(4)
# print(s)

#test = (1,2,[10,11,12])
# x = list(test)
# x.append(5)
# test = tuple(x)
# print(test)

# dic = \
#     {
#     "Vlad" : 170,
#     "Milan" : 194,
#     "Vyacheslav" : 182
# }
# x = "Vyacheslav"
# # if x in dic:
# #     print(dic[x])
#
# # print(dic.get("Milan", "Does not exist!"))
#
# dict = {input("Enter name:"), int(input("Enter height:"))}
# print(dict)

# key = "a"
# value = 15
# dict = {key:value}
# dict[key] = "b"
# dict["bomba"] = "c"
# # for item in dict.items():
# #     print(item)
# print(dict.popitem("bomba"))
# print(dict)
#from copy import deepcopy
# st1 = [1,2,[1,2,3,4]]
# st2 = deepcopy(st1)
# st2[-1].append(5)
# print(st1,st2)
# mylist = {1,2,2,3,4,5,5}
# mylist2 = {2,4,4,5}
# print(mylist == mylist2)
# print(mylist & mylist2)


# По данному целому числу N распечатайте все квадраты натуральных чисел,
# не превосходящие N,
# в порядке возрастания.

# x = int(input())
# index = 1
# while index ** 2 <= x:
#     print(index ** 2)
#     index += 1


# Дано целое число, не меньшее 2.
# Выведите его наименьший натуральный делитель,
# отличный от 1.

# x = int(input())
# u = 2
# while x % u:
#     u+=1
# else:
#     print(u)

# По данному натуральному числу N найдите наибольшую целую степень двойки,
# не превосходящую N. Выведите показатель степени и саму степень.
# Операцией возведения в степень пользоваться нельзя!

# n = int(input())
# i = 1
# res = 2
# while res*2 < n:
#     i+=1
#     res*=2
# else:
#     print(i, res)


# В первый день спортсмен пробежал x километров, а затем он каждый день увеличивал пробег на 10% от предыдущего значения.
# По данному числу y определите номер дня, на который пробег спортсмена составит не менее y километров.
# Программа получает на вход действительные числа x и y и должна вывести одно натуральное число.

# x = int(input())
# y = int(input())
# res = 1
# while x < y:
#     x += x/10
#     res += 1
# else:
#     print(res)


# Программа получает на вход последовательность целых неотрицательных чисел,
# каждое число записано в отдельной строке.
# Последовательность завершается числом 0,
# при считывании которого программа должна закончить свою работу и вывести количество членов последовательности
# (не считая завершающего числа 0). Числа, следующие за числом 0, считывать не нужно.
# res = 0
# while int(input()):
#     res +=1
# else:
#     print(res)

# Определите сумму всех элементов последовательности, завершающейся числом 0.
# В этой и во всех следующих задачах числа, следующие за первым нулем, учитывать не нужно.


# res = 0
# s = True
# while s:
#     x = int(input())
#     if x:
#         res += x
#     else:
#         s = False
# else:
#     print(res)


# Определите среднее значение всех элементов последовательности, завершающейся числом 0.

# res = 0
# index = 0
# s = True
# while s:
#     x = int(input())
#     if x:
#         res += x
#         index += 1
#     else:
#         s = False
# else:
#     print(res/index)

# Последовательность состоит из натуральных чисел и завершается числом 0.
# Определите значение наибольшего элемента последовательности.

# res = 0
# s = True
# while s:
#     x = int(input())
#     if x > res:
#         res = x
#     elif x:
#         pass
#     else:
#         s = False
# else:
#     print(res)

# Последовательность состоит из натуральных чисел и завершается числом 0.
# Определите индекс наибольшего элемента последовательности.
# Если наибольших элементов несколько, выведите индекс первого из них.
# Нумерация элементов начинается с нуля.

# res = 0
# index = -1
# index2 = -1
# s = True
# while s:
#     x = int(input())
#     if x > res:
#         res = x
#         index += 1
#         index2 = index
#     elif x:
#         index += 1
#     else:
#         s = False
# else:
#     print(index2)

# res = 0
# s = True
# while s:
#     x = int(input())
#     if x % 2:
#         continue
#     elif not x:
#         s = False
#     else:
#         res += 1
# else:
#     print(res)

# Последовательность состоит из натуральных чисел и завершается числом 0.
# Определите, сколько элементов этой последовательности больше предыдущего элемента.

# res = 0
# prev = 0
# s = True
# while s:
#     x = int(input())
#     if not x:
#         s = False
#     else:
#         if x > prev and prev:
#             res+=1
#         prev = x
# else:
#     print(res)


# Последовательность состоит из натуральных чисел и завершается числом 0.
# Определите, сколько элементов этой последовательности равны ее наибольшему элементу.

# max = 0
# list = []
# s = True
# while s:
#     x = int(input())
#     if not x:
#         s = False
#     else:
#         if x > max:
#             max = x
#         list.append(x)
# else:
#     print(list.count(max))

# res = 0
# list = []
# prev = int(input())
# while prev:
#     next = int(input())
#     if next:
#         while next == prev:
#             res += 1
#         else:

# Выведите все элементы списка с четными индексами (то есть A[0], A[2], A[4], ...).

# list = list(input().split())
# for index, value in enumerate(list):
#     if not index % 2:
#         print(value)

# Выведите все четные элементы списка.
# При этом используйте цикл for, перебирающий элементы списка, а не их индексы!

# list = list(input().split())
# for v in list:
#     if not int(v) % 2:
#         print(v)

# Дан список чисел. Выведите все элементы списка, которые больше предыдущего элемента.

# list = list(input().split())
# for i in range(len(list)):
#     if int(list[i]) > int(list[i-1]) and i != 0:
#         print(list[i])

# Дан список чисел. Если в нем есть два соседних элемента одного знака, выведите эти числа.
# Если соседних элементов одного знака нет — не выводите ничего.
# Если таких пар соседей несколько — выведите первую пару.

# list = list(input().split())
# for i in range(len(list)-1):
#     if (int(list[i]) < 0 and int(list[i+1]) < 0) or (int(list[i]) > 0 and int(list[i+1]) > 0):
#         print(list[i], list[i+1])
#         break

# Дан список чисел. Определите, сколько в этом списке элементов, которые больше двух своих соседей, и выведите количество таких элементов.
# Крайние элементы списка никогда не учитываются, поскольку у них недостаточно соседей.

# list = list(input().split())
# res = 0
# for i in range(1, len(list) - 1):
#     if int(list[i]) > int(list[i-1]) and int(list[i]) > int(list[i+1]):
#         res +=1
# else:
#     print(res)

# Дан список чисел. Выведите значение наибольшего элемента в списке, а затем индекс этого элемента в списке.
# Если наибольших элементов несколько, выведите индекс первого из них.
#
# list = [int(i) for i in input().split()]
# res = list[0]
# index = 0
# for i in range(len(list)):
#     if list[i] > res:
#         res = list[i]
#         index = i
# else:
#     print(res, index)

# Петя перешёл в другую школу. На уроке физкультуры ему понадобилось определить своё место в строю. Помогите ему это сделать.
# Программа получает на вход невозрастающую последовательность натуральных чисел, означающих рост каждого человека в строю.
# После этого вводится число X – рост Пети. Все числа во входных данных натуральные и не превышают 200.
# Выведите номер, под которым Петя должен встать в строй.
# Если в строю есть люди с одинаковым ростом, таким же, как у Пети, то он должен встать после них.

# list = [int(i) for i in input().split()]
# x = int(input())
# for i,v in enumerate(list):
#     if x > v:
#         print(i+1)
#         break
# else:
#     print(len(list)+1)

# Дан список, упорядоченный по неубыванию элементов в нем. Определите, сколько в нем различных элементов.

# list = [int(i) for i in input().split()]
# print(len(set(list)))


# Переставьте соседние элементы списка (A[0] c A[1], A[2] c A[3] и т. д.).
# Если элементов нечетное число, то последний элемент остается на своем месте.

# list = [int(i) for i in input().split()]
# res = ""
# for i,v in enumerate(list):
#     if not i % 2:
#         try:
#             list[i] = list[i+1]
#             list[i+1] = v
#         except IndexError:
#             pass
# else:
#     for v in list:
#         res += f"{v} "
#     else:
#         print(res)

### ИЛИ

# list = [int(i) for i in input().split()]
# list2 = []
# res = ""
# for i,v in enumerate(list):
#     if not i % 2:
#         try:
#             list2.append(list[i+1])
#             list2.append(v)
#         except IndexError:
#             list2.append(v)
# else:
#     for v in list2:
#         res += str(v)
#         res += " "
# print(res)

### ИЛИ

# list = [int(i) for i in input().split()]
# list2 = []
# for i,v in enumerate(list):
#     if not i % 2:
#         try:
#             list2.append(list[i+1])
#             list2.append(v)
#         except IndexError:
#             list2.append(v)
# else:
#     print(" ".join(str(i) for i in list2))

# В списке все элементы различны. Поменяйте местами минимальный и максимальный элемент этого списка.

# list = [int(i) for i in input().split()]
# min = list[0]
# imin = 0
# max = list[0]
# imax = 0
# res = list.copy()
# for i,v in enumerate(list):
#     if v < min:
#         min = v
#         imin = i
#     elif v > max:
#         max = v
#         imax = i
#     else:
#         continue
# else:
#     res[imin], res[imax] = res[imax], res[imin]
#     print(" ".join(str(i) for i in res))

# Дан список из чисел и индекс элемента в списке k.
# Удалите из списка элемент с индексом k,
# сдвинув влево все элементы, стоящие правее элемента с индексом k.
# Программа получает на вход список, затем число k.
# Программа сдвигает все элементы, а после этого удаляет последний элемент списка
# при помощи метода pop() без параметров.
#
# Программа должна осуществлять сдвиг непосредственно в списке,
# а не делать это при выводе элементов.
# Также нельзя использовать дополнительный список.
# Также не следует использовать метод pop(k) с параметром.

# list1 = [int(i) for i in input().split()]
# index = int(input())
# list1.pop(index)
# print(" ".join(str(i) for i in list1))

# list1 = [int(i) for i in input().split()]
# res = []
# k = int(input())
# for i,v in enumerate(list1):
#     if i==k:
#         pass
#     else:
#         res.append(v)
# else:
#     print(" ".join(str(i) for i in res))

# Дан список целых чисел, число k и значение C.
# Необходимо вставить в список на позицию с индексом k элемент, равный C,
# сдвинув все элементы, имевшие индекс не менее k, вправо.
# Поскольку при этом количество элементов в списке увеличивается,
# после считывания списка в его конец нужно будет добавить новый элемент,
# используя метод append.
#
# Вставку необходимо осуществлять уже в считанном списке, не делая этого при выводе и не
# создавая дополнительного списка.

# list = [int(i) for i in input().split()]
# u = [int(i) for i in input().split()]
# for index in range(len(list)+1):
#     if index == u[0]:
#         list.insert(u[0],u[1])
# else:
#     print(" ".join(str(i) for i in list))

#Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу.
# Считается, что любые два элемента, равные друг другу образуют одну пару,
# которую необходимо посчитать.

# list = [int(i) for i in input().split()]
# list2 = []
# res = 0
# for i,v in enumerate(list):
#     for ind, val in enumerate(list):
#         if ind==i:
#             continue
#         else:
#             if v==val:
#                 res+=1
#             else:
#                 continue
# print(res//2)

# Дан список. Выведите те его элементы, которые встречаются в списке только один раз.
# Элементы нужно выводить в том порядке, в котором они встречаются в списке.

# list1 = [int(i) for i in input().split()]
# list2 = []
# for v in list1:
#     if list1.count(v) == 1:
#         list2.append(v)
# print(" ".join(str(i) for i in list2))

# Дан список чисел. Определите, сколько в нем встречается различных чисел.
# Примечание. Эту задачу на Питоне можно решить в одну строчку.

# list = [int(i) for i in input().split()]
# print(len(set(list)))

# Даны два списка чисел.
# Посчитайте, сколько чисел содержится одновременно как в первом списке,
# так и во втором.
# Примечание. Эту задачу на Питоне можно решить в одну строчку.

# list1 = [int(i) for i in input().split()]
# list2 = [int(i) for i in input().split()]
# print(len(set(list1).intersection(set(list2))))

# Даны два списка чисел. Найдите все числа, которые входят как в первый,
# так и во второй список и выведите их в порядке возрастания.
#
# Примечание. И даже эту задачу на Питоне можно решить в одну строчку.

# list1 = [int(i) for i in input().split()]
# list2 = [int(i) for i in input().split()]
# print(" ".join(str(i) for i in sorted(set(list1).intersection(list2))))

# list1 = list(map(int, input().split()))
# print(list1)

# Во входной строке записана последовательность чисел через пробел.
# Для каждого числа выведите слово YES (в отдельной строке),
# если это число ранее встречалось в последовательности или NO, если не встречалось.

# list1 = list(map(int,input().split()))
# list2 = []
# for v in list1:
#     if v not in list2:
#         list2.append(v)
#         print("NO")
#     else:
#         print("YES")

# В первой строке входных данных записаны числа N и M — число кубиков у Ани и Бори.
# В следующих N строках заданы номера цветов кубиков Ани.
# В последних M строках номера цветов Бори.

# Найдите три множества: номера цветов кубиков, которые есть в обоих наборах;
# номера цветов кубиков, которые есть только у Ани и номера цветов кубиков,
# которые есть только у Бори. Для каждого из множеств выведите сначала количество
# элементов в нем, а затем сами элементы, отсортированные по возрастанию.

# n,m = [int(i) for i in input().split()]
# s1 = set()
# s2 = set()
# for i in range(n):
#     s1.add(int(input()))
# for i in range(m):
#     s2.add(int(input()))
# u = s1.intersection(s2)
# a = s1.difference(s2)
# b = s2.difference(s1)
# for sett in u,a,b:
#     print(len(sett))
#     for v in sorted(sett):
#         print(v)

# Дан текст: в первой строке записано число строк, далее идут сами строки.
# Определите, сколько различных слов содержится в этом тексте.
#
# Словом считается последовательность непробельных символов идущих подряд,
# слова разделены одним или большим числом пробелов или символами конца строки.

# n = int(input())
# slova = set()
# for i in range(n):
#     [slova.add(i) for i in input().split()]
# else:
#     print(len(slova))

# Август и Беатриса играют в игру. Август загадал натуральное число от 1 до n.
# Беатриса пытается угадать это число, для этого она называет некоторые множества натуральных чисел.
# Август отвечает Беатрисе YES, если среди названных ей чисел есть задуманное или NO в противном случае.
# После нескольких заданныъх вопросов Беатриса запуталась в том, какие вопросы она задавала и какие ответы получила
# и просит вас помочь ей определить, какие числа мог задумать Август.
#
# В первой строке задано n - максимальное число, которое мог загадать Август.
# Далее каждая строка содержит вопрос Беатрисы (множество чисел, разделенных пробелом) и ответ Августа на этот вопрос.
#
# Вы должны вывести через пробел, в порядке возрастания, все числа, которые мог задумать Август.

# n = int(input())
# ask = set(list(i for i in input().split()))
# res = ask.copy()
# while True:
#     if not "HELP" in ask:
#         answer = input()
#         if answer == "YES":
#             res.intersection_update(ask)
#             ask = set(list(i for i in input().split()))
#         elif answer == "NO":
#             res.difference_update(ask)
#             ask = set(list(i for i in input().split()))
#     else:
#         print(" ".join(i for i in sorted(res)))
#         break

# set1 = {3, 5, 9}
# set2 = {1, 15, 6, 9}
# set1.difference_update(set2)
# print(set1)


# total_shk = int(input())
# obsh = []
# zn_vse = set()
# zn_odin = set()
# for i in range(total_shk):
#     lang_count = int(input())
#     for ind in range(lang_count):
#         obsh.append(input())
# else:
#     for lan in obsh:
#         if obsh.count(lan) == total_shk:
#             zn_vse.add(lan)
#             zn_odin.add(lan)
#         else:
#             zn_odin.add(lan)
#     else:
#         print(len(zn_vse))
#         for i in sorted(zn_vse):
#             print(i)
#         print(len(zn_odin))
#         for i in sorted(zn_odin):
#             print(i)

# words = input().split()
# dic = {}
# for v in words:
#     if not v in dic:
#         dic[v] = 0
#     else:
#         dic[v]+=1
#     print(dic.get(v, 0))

# Вам дан словарь, состоящий из пар слов. Каждое слово является синонимом к парному ему слову. Все слова в словаре различны.
# Для слова из словаря, записанного в последней строке, определите его синоним.

# dic = {}
# n = int(input())
# for i in range(n):
#     words = input().split()
#     dic[words[1]] = words[0]
#     dic[words[0]] = words[1]
# else:
#     print(dic[input()])

# В первой строке дано количество записей.
# Далее, каждая запись содержит фамилию кандидата и число голосов,
# отданных за него в одном из штатов.
# Подведите итоги выборов: для каждого из участника голосования определите число
# отданных за него голосов. Участников нужно выводить в алфавитном порядке.

#dic = {}
# n = int(input())
# for i in range(n):
#     name,numbers = input().split()
#     dic[name] = (dic.get(name, 0)) + int(numbers)
# else:
#     [print(i[0],i[1]) for i in sorted(dic.items())]

# Дан текст: в первой строке задано число строк, далее идут сами строки.
# Выведите слово, которое в этом тексте встречается чаще
# всего. Если таких слов несколько, выведите то, которое меньше в лексикографическом порядке.

# dic = {}
# n = int(input())
# max = 0
# for i in range(n):
#     inp = input().split()
#     for v in inp:
#         dic[v] = dic.get(v,0) + 1
#         if dic[v] >= max:
#             max = dic[v]
# else:
#     for item in sorted(dic.items()):
#         if item[1] == max:
#             print(item[0])
#             break

# В первой строке содержится число N — количество файлов содержащихся
# в данной файловой системе. В следующих N строчках содержатся имена
# файлов и допустимых с ними операций, разделенные пробелами.
# Далее указано чиcло M — количество запросов к файлам.
# В последних M строках указан запрос вида Операция Файл.
# К одному и тому же файлу может быть применено любое колличество запросов.
#
# Вам требуется восстановить контроль над правами доступа к файлам
# (ваша программа для каждого запроса должна будет возвращать OK если над
# файлом выполняется допустимая операция, или же Access denied,
# если операция недопустима.

# commands = {"write":"W","read":"R","execute":"X"}
# dic = {}
# n = int(input())
# for _ in range(n):
#     line = input().split()
#     for ind, word in enumerate(line):
#         if not ind:
#             dic[word] = list()
#         else:
#             dic[line[0]].append(word)
# else:
#     m = int(input())
#     for _ in range(m):
#         line = input().split()
#         command = commands[line[0]]
#         if command in dic[line[1]]:
#             print("OK")
#         else:
#             print("Access denied")

# results = {}
# n = int(input())
# for _ in range(n):
#     words = input().split()
#     for word in words:
#         results[word] = results.get(word,0) + 1
# for res in sorted(results.items(), key=lambda x: (-x[1],x[0])):
#     print(res[0])



