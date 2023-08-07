from base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey, Integer

class Director(Base):
    __tablename__ = 'Directors'
    id:Mapped[int] = mapped_column(primary_key=True, autoincrement=True, nullable=False)
    name:Mapped[str] = mapped_column(String(30), nullable=False)
    surname:Mapped[str] = mapped_column(String(30), nullable=False)
    age:Mapped[int] = mapped_column(nullable=False)
    profession:Mapped[str] = mapped_column(String(30), nullable=False, default="Director")
    balance:Mapped[float] = mapped_column(nullable=False, default=0)

    # def __str__(self):
    #     return f'{self.id}, {self.name}, {self.surname}, {self.age}, {self.profession}, {self.balance}'
    #
    # def __repr__(self):
    #     return f'{self.id}, {self.name}, {self.surname}, {self.age}, {self.profession}, {self.balance}'

class Zavuch(Base):
    __tablename__ = 'Zavuches'
    id:Mapped[int] = mapped_column(primary_key=True, autoincrement=True, nullable=False)
    name:Mapped[str] = mapped_column(String(30), nullable=False)
    surname:Mapped[str] = mapped_column(String(30), nullable=False)
    age:Mapped[int] = mapped_column(nullable=False)
    profession:Mapped[str] = mapped_column(String(30), nullable=False, default="Zavuch")
    balance:Mapped[float] = mapped_column(nullable=False, default=0)


class Teacher(Base):
    __tablename__ = 'Teachers'
    id:Mapped[int] = mapped_column(primary_key=True, autoincrement=True, nullable=False)
    name:Mapped[str] = mapped_column(String(30), nullable=False)
    surname:Mapped[str] = mapped_column(String(30), nullable=False)
    age:Mapped[int] = mapped_column(nullable=False)
    profession:Mapped[str] = mapped_column(String(30), nullable=False, default="Teacher")
    balance:Mapped[float] = mapped_column(nullable=False, default=0)


class Student(Base):
    __tablename__ = 'Students'
    id:Mapped[int] = mapped_column(primary_key=True, autoincrement=True, nullable=False)
    name:Mapped[str] = mapped_column(String(30), nullable=False)
    surname:Mapped[str] = mapped_column(String(30), nullable=False)
    age:Mapped[int] = mapped_column(nullable=False)
    profession:Mapped[str] = mapped_column(String(30), nullable=False, default="Student")
    balance:Mapped[float] = mapped_column(nullable=False, default=0)


class School(Base):
    __tablename__ = 'Schools'
    id:Mapped[int] = mapped_column(primary_key=True, autoincrement=True, nullable=False)
    name:Mapped[str] = mapped_column(String(30), nullable=False)
    classes:Mapped[str] = mapped_column(String(255))


class Class(Base):
    __tablename__ = 'Classes'
    id:Mapped[int] = mapped_column(primary_key=True, autoincrement=True, nullable=False)
    name:Mapped[str] = mapped_column(String(30), nullable=False)
    students:Mapped[str] = mapped_column(String(255))
    class_manager:Mapped[str] = mapped_column(String(30), nullable=False)
