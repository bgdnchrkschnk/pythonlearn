from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    def __str__(self):
        return f'{self.id}, {self.name}, {self.surname}, {self.age}, {self.profession}, {self.balance}'

    def __repr__(self):
        return f'{self.id}, {self.name}, {self.surname}, {self.age}, {self.profession}, {self.balance}'

class DBExistError(Exception):
    pass
