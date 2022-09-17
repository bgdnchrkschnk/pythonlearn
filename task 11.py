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

# # from typing import iterable
# def remove_all_before(items: list, border: int):
#     for i, val in enumerate(items):
#         if val==border:
#             return items[i:]
#             break
#     return items
# print(remove_all_before([3,5,3,4,0,3,6,5],0))
#
# import string
# def is_all_upper(text: str) -> bool:
#     return text.upper() == text
# print(is_all_upper("VVV"))

# def replace_first(items: list):
#     try:
#         items.append(items.pop(0))
#         return items
#     except IndexError:
#         return items
#
# print(replace_first([]))


# def max_digit(a: int) -> int:
#   return int(max(str(a)))
#
# print(max_digit(3267869509979000)


# def beginning_zeros(a: str) -> int:
#     counter = 0
#     for v in a:
#         if v == "0":
#             counter += 1
#         else:
#             break
#     return counter
#
# print(beginning_zeros("0000067248789"))

# def between_markers(text: str, start: str, end:str) -> str:
#     start_index = text.find(start)
#     end_index = text.find(end)
#     return text[start_index+1:end_index]
#
# print(between_markers('What is >apple<', '>', '<'))

# def split_pairs(text: str):
#     list = []
#     for index, value in enumerate(text):
#             if index % 2 == 0:
#                 try:
#                     list.append(text[index]+text[index+1])
#                 except IndexError:
#                     list.append(text[index] + "_")
#     return list
# print(split_pairs("eubiuhifwef"))

# def correct_sentence(text: str) -> str:
#     if not text[0].isupper():
#         text = text[0].upper() + text[1:]
#     if text[-1] != ".":
#         text += "."
#     return text
#
# print(correct_sentence("greetings, friends"))


def is_even(num: int) -> bool:
    if not num % 2:
        return True
    else:
        return False

print(is_even(5))

def nearest_value(values: set, one: int) -> int:
    return min(values, key=lambda n:(abs(one - n), n))

print(nearest_value({4, 7, 10, 11, 12, 17}, 9))

a = lambda x: x/2
print(a(5))
