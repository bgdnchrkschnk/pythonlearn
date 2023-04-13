class xDPoint:
    def __init__(self, x:int, y:int, z:int):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        if isinstance(other, self.__class__):
            return self.__class__(self.x + other.x, self.y + other.y, self.z + other.z)
        elif isinstance(other, int):
            self.x += other
            self.y += other
            self.z += other
        else:
            raise TypeError("Adding can be performed only between two xDPoints!")

    def __sub__(self, other):
        if isinstance(other, self.__class__):
            return self.__class__(self.x - other.x, self.y - other.y, self.z - other.z)
        elif isinstance(other, int):
            self.x -= other
            self.y -= other
            self.z -= other
        else:
            raise TypeError("Substracting can be performed only between two xDPoints!")

    def __mul__(self, other):
        if isinstance(other, int):
            self.x *= other
            self.x *= other
            self.z *= other
        else:
            raise TypeError("Adding can be performed only between two xDPoints!")

    def __truediv__(self, other):
        if isinstance(other, int):
            self.x = int(self.x / other)
            self.y = int(self.y / other)
            self.z = int(self.z / other)
        else:
            raise TypeError("Adding can be performed only between two xDPoints!")

    def __repr__(self):
        return f"{self.__class__.__name__} with coordinates x={self.x}, y={self.y}, z={self.z}"


a = xDPoint(6,2,4)
b = xDPoint(1,0,0)
a/2
print(a)


