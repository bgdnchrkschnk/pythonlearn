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

