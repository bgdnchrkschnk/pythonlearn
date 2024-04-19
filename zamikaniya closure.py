import random

# str = "Denis"

def main():
    # str = "Bogdan"

    def text(t="Hello"):
        # str = "yefuwbjb"
        print(type())

    text()

main()


# func2 = main("Slavik")
# func2("Fuck you")
#
#
# def initialize():
#     counter = 0
#
#     def wrapper(name=None):
#         nonlocal counter
#         counter += 1
#         print(f"Welcome, {name}!")
#         return counter
#
#     return wrapper
#
#
# inn = initialize()
# print(inn("Bohdan"))
# print(inn())
# print(inn())
#
# from time import perf_counter
#
#
# def timer_func():
#     first_time = perf_counter()
#
#     def wrapper():
#         print(perf_counter() - first_time)
#
#     return wrapper


# nn = timer_func()
# nn()
# nn()


# def add(a, b):
#     return a + b
#
#
# def counter(func):
#     count = 0
#
#     def wrapper(*args, **kwargs):
#         nonlocal count
#         count += 1
#         print(f"Function {func.__name__} called for {count} times!")
#         return func(*args, **kwargs)
#
#     return wrapper
#
# r = counter(add)
# r(1, 2)
# r(4, 14)

