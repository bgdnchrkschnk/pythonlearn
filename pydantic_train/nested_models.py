import json
from typing import Optional

from pydantic import BaseModel, EmailStr, PositiveInt, HttpUrl, conlist, Field


class Hobbie(BaseModel):
    name: str = None
    description: str
    recommendations: list[str] | None


class User(BaseModel):
    name: str = "unnamed"
    sex: str = Field(alias="gender")
    age: PositiveInt
    email: EmailStr | None
    account_link: Optional[HttpUrl]
    married: bool
    hobbies: list[Hobbie | None]


class School(BaseModel):
    name: str
    classes: conlist(str, min_length=4)
    students: conlist(User, min_length=1)


singing_dict = {"name":"Singing",
                "description": "Musician hobbie when person sings",
                "recommendations": ["Regular trainings",
                                    "Drink warm water",
                                    "Sleep well"]
                }


singing = Hobbie(**singing_dict)


bogdan_dict = {"name": "Bogdan",
               "gender": "male",
               "age": 18,
               "email": "testemail@gmail.com",
               "married": True,
               "account_link": "https://vk.com",
               "hobbies": [singing]}


bogdan = User(**bogdan_dict)

print(bogdan.model_dump_json(indent=True, exclude="married"))


my_school_dict = {"name": "Lanzheronovskiy liceum",
                  "classes": ["10-A", "10-B", "11-A", "11-B", "10-A"],
                  "students": [bogdan]}

my_school = School(**my_school_dict)

print(my_school.model_dump_json(indent=True))
