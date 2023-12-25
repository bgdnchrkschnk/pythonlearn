# #WRONG
# def func(a=tuple()):
#     return a, type(a)
# ###
#
#
# def func2(a = None):
#     a = tuple() if not a else a
#     return a, type(a)
#
# print(func2([1,2,3]))
#
#
# def foo(numb):
#     res = list()
#     for _ in range(0, numb, 2):
#         res.append(_)
#     return res
#
# print(foo(16))


# d = {"f": 1, "s": 2}
# for item in d.items():
#     print(item)

# l = map(lambda x: x**3, d.values())
# print(tuple(l))
# f = filter(lambda x: x!="f", d)
# print(tuple(f))

from copy import deepcopy
list1 = [1,2,3,4,5]
list2 = [6,7,8,9,10]

def func_map(x):
    res = x-1
    return res

res_map = map(func_map, list1)

def func_filter(x):
    return not x%2

res_filter = filter(func_filter, list1)

res_zip = zip(list1, list2)

print(list(res_map))
print(list(res_filter))
print(list(res_zip))

