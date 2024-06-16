import random
from typing import Optional
from uuid import uuid4

from pydantic import BaseModel, EmailStr, PositiveInt, HttpUrl, Field


def get_random_married():
    values = [True, False]
    return random.choice(values)


class User(BaseModel):
    id: int | str = Field(default_factory=lambda: uuid4().hex)
    name: str = "unnamed"
    sex: str
    age: PositiveInt
    email: EmailStr | None
    account_link: Optional[HttpUrl]
    married: bool = Field(default_factory=get_random_married)
    hobbies: Optional[list[str]]


bogdan_dict = {"name": "Bogdan",
               "sex": "male",
               "age": 18,
               "email": "testemail@gmail.com",
               "account_link": "https://vk.com",
               "hobbies": ["singing"]}

bogdan = User(**bogdan_dict)

print(bogdan.model_dump_json(indent=True))