# def mult_two(one:int, two:int) -> int:
#     x = one*two
#     return x
# print(mult_two(2,5))

# def first_word(text:str) -> str:
#     frst = text.split()[0]
#     return str(frst)
# print(first_word("hello kitt"))

# def is_acceptable_password(password: str) -> bool:
#     return len(password) > 6
#
# print(is_acceptable_password("njifdtnrnrt"))

# def number_length(a: int) -> int:
#     return len(str(a))
#
# print(number_length(-5455553453235))

# def most_frequent(data):
#     return max((data), key = data.count)
#
# print(most_frequent(["a", "a", "z", "b", "a", "b"]))

#def backward_string(val: str) -> str:
#     return val[::-1]
#
# print(backward_string("Ukraine fucks russia!"))

# def end_zeros(numb: int) -> int:
#     counter = 0
#     for num in str(numb)[::-1]:
#         if num == str(0):
#             counter +=1
#         else:
#             break
#     return counter
#
# print(end_zeros(100100000))

# def easy_unpack(elements: tuple) -> tuple:
#     return (elements[0], elements[2], elements[-2])
#
# print(easy_unpack((2,4,3,5,4,3,2)))

# from typing import iterable
def remove_all_before(items: list, border: int):
    for i, val in enumerate(items):
        if val==border:
            return items[i:]
            break
    return items
print(remove_all_before([3,5,3,4,0,3,6,5],0))

