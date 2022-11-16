# class Triangle:
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def __repr__(self):
#         return f"[{self.a}, {self.b}, {self.c}]"
#
#     def __add__(self, other):
#         new_a = self.a + other.a
#         new_b = self.b + other.b
#         new_c = self.c + other.c
#         return Triangle(new_a, new_b, new_c)
#
#     def _sq(self):
#         return self.a * self.b * self.c
#
#     def __eq__(self, other):
#         return self.a == other.a and self.b == other.b and self.c == other.c
#
# tr1 = Triangle(5,5,10)
# tr2 = Triangle(4,3,9)
# tr3 = tr1 + tr2
# tr4 = tr2
# # print(tr3.a, tr3.b, tr3.c)
# tr_test = Triangle(4,3,9)
# # res = []
# # tr_list = [tr1, tr2, tr3, tr4]
# # for tr in tr_list:
# #     if tr == tr_test:
# #         res.append(tr)
# # print(res)
#
# print(tr2 == tr4)
#
#

class Rec:
    def __init__(self, w, h):
        self.w = w
        self.h = h
        self._sq = self.sq

    @property
    def sq(self):
        return self.w * self.h

rec1 = Rec(5,7)
print(rec1.sq)