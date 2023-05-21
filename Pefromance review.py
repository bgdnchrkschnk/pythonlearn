# try:
#     print(3+"hhh")
# except TypeError:
#     print("except TypeError")
# #else виконується в випадку, якщо except блоки не були задіяні:
# # обовʼязково має бути присутній хочаб один except в конструкції
# else:
#     print("everything is good")
# #finally виконується усіх випадках конструкції
# finally:
#     print("finally")


# def kvadrat_chysla(x):
#     return x ** 2
#
# print(kvadrat_chysla(16))
#
# def mnojennya(x,y):
#     return x * y
#
# print(mnojennya(5,6))
#
# def plus(x,y,z):
#     return x,y,z
#
# print(plus(z=5,y=3,x=1))
#
# def prin(a,b,c="default"):
#     return a+b+c
#
# def prin(a,b,c="def"):
#     return a+b+c
# print(prin("1","2",c="8"))
#
# def plus(*args, **kwargs):
#     res = 0
#     for v in args:
#         res+=v
#     else:
#         print(res)
#         print(kwargs)
#
# plus(1,2,3,4,5, c=0)
#
# a = [1,5,2,3,5,6]
# print(*a)
# #
# a,*b,c = True, 5, 16, "good"
# print(a,b,c)
#
# lis = [5,12]
# print(tuple(range(*lis)))
#
#
# def test(*args, res=99, **kwargs):
#     for item in kwargs:
#         print(kwargs[item])
#     print(args,kwargs, res)
#
# test(6,7,4, re=100)


import json

dic = {"name":"John", "age":30, "car":None, "examples":{"firstname":1, "secondname":2}}

dic_json = json.dumps(dic)
print(dic_json, type(dic_json))

dicc = json.loads(dic_json)
print(dicc, type(dicc))
print(dicc["examples"]["firstname"])