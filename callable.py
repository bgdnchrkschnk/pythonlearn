# f = lambda : "hi"
# print(callable(f))
# print(f())
# #True
#
# def square(x):
#     return x**2
# print(callable(square))
# #True
#
# x = 3
# print(callable(x))
# #False
#
# class C:
#     def __init__(self, x):
#         self.x = x
# print(callable(C))
# #True
#
# obj = C(3)
# print(callable(obj))
# #False
#
# lst = [1,2,3]
# print(callable(lst.append))
#
#
# def func():
#     for i in range(10):
#         yield i
#
# print()
#
#
#
# from functools import wraps
#
# class multiplier:
#     def __init__(self, multiplier:int):
#         self.multiplier = multiplier
#
#     def __call__(self, func):
#         def wrapper(*args, **kwargs):
#             new_args = [arg * self.multiplier for arg in args]
#             new_kwargs = {k:v * self.multiplier for k,v in zip(dict(kwargs).keys(), dict(kwargs).values())}
#             return func(*new_args, **new_kwargs)
#         return wrapper
#
# @multiplier(2)
# def plus(a,b):
#     return a+b
#
# print(plus(2,3))
#
#
#
#
#
# class Decorator:
#     def __init__(self,func):
#         self.function=func
#
#     def __call__(self, *args, **kwargs):
#         result=self.function(*args,**kwargs)
#         return result * 2
#
# @Decorator
# def sum(*args):
#     res = 0
#     for arg in args:
#         res+=arg
#     return res
#
# print(sum(2,3))

from functools import wraps
# class Big:
#     def __init__(self, numbers):
#         self.numbers = numbers
#
#     def __call__(self, func):
#             def wrapper(arg):
#                 res = func(arg)
#                 print(res[:self.numbers].upper() +res[self.numbers:])
#             return wrapper
#
# @Big(3)
# def pprint(arg:str):
#     return str(arg)
#
# pprint("hello, my baby")
#
#
#
#
#
#
#
# x = Big(3)
# print(x("hello world!"))

# def split_ret(func):
#     def wrapper():
#         return func().split()
#     return wrapper
#
#
# @split_ret
# def ret():
#     return "hello kitty boy"
#
# print(ret())


class Check_div:
    def __init__(self, number):
        self.number = number
    def __call__(self, func):
        def wrapper(*args):
            if self.number in args:
                raise TypeError(f"This number in unavaliable!")
            else:
                return int(func(*args))
        return wrapper




@Check_div(4)
def div(a:int,b:int):
    return a/b

print(div(3,1))
