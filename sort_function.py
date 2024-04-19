x = [1, 22, -5, 19, 0]


def sort_list_ascending(l: list = None):
    if isinstance(l, list):
        res = list()
        for _ in range(len(l)):
            max_numb = max(l)
            res.append(max_numb)
            l.remove(max_numb)
    else:
        raise TypeError("List is expected as argument into this function!")
    return res


def sort_list_descending(l: list = None):
    if l:
        if isinstance(l, list):
            res = list()
            for _ in range(len(l)):
                min_numb = min(l)
                res.append(min_numb)
                l.remove(min_numb)
        else:
            raise TypeError("List is expected as argument into this function!")
        return res
    else:
        return None


print(sort_list_descending(x))
print([] or [


























    ]\
])
