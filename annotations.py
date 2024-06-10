from typing import Union, Optional, Any, Final, Callable, List

digit: Union[int, float]
digit: int | float

number: Optional[int] = 5
number: int | None

digits: Any

CONST: Final = 5

lst: list[int | float] = [5.5]

tpl: tuple[int, str | float, list] = (5, 5.3, [])  # annotation for each value
tpl1: tuple[int, ...] = (1, 2, 3)  # ... means any number of values

dct: dict[str, int] = {"one": 1,
                       "two": 2}  # str, int annotation for dict key and value

st: set[str | None] = {None, "word"}


def get_digits(func: Callable[[int], list], lst: list[int] | None) -> list[int | None] | None:
    if list:
        res = filter(func, lst)
        return list(res)
    return []


print(get_digits(func=lambda x: x > 0, lst=[-1, -2, 3, -4, 5, 0]))
