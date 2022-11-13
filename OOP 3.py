class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __add__(self, other):
        new_a = self.a + other.a
        new_b = self.b + other.b
        new_c = self.c + other.c
        return Triangle(new_a, new_b, new_c)

tr1 = Triangle(5,5,10)
tr2 = Triangle(4,3,9)
tr3 = tr1 + tr2
print(tr3.a, tr3.b, tr3.c)