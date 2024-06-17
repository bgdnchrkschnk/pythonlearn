import json
import random
from typing import Optional
from uuid import uuid4
from pydantic_core._pydantic_core import ValidationError

from pydantic import BaseModel, EmailStr, PositiveInt, HttpUrl, Field, computed_field


def get_random_married():
    values = [True, False]
    return random.choice(values)


class User(BaseModel):
    id: int | str = Field(default_factory=lambda: uuid4().hex)
    name: str = "unnamed"
    sex: str = Field(min_length=2, max_length=12, alias="gender")
    age: PositiveInt
    email: EmailStr | None
    account_link: Optional[HttpUrl]
    married: bool = Field(default_factory=get_random_married)
    hobbies: Optional[list[str]]

    @computed_field
    @property
    def test(self) -> int:
        return self.age * 10


bogdan_dict = {"name": "Bogdan",
               "gender": "male",
               "age": 18,
               "email": "testemail@gmail.com",
               "account_link": "https://vk.com",
               "hobbies": ["singing"]}

bogdan = User(**bogdan_dict)

with open("../test.json", "r") as f:
    global json_obj
    json_obj = f.read()


js = json.loads(json_obj)
try:
    user = User.model_validate(js)
except ValidationError as err:
    raise err
else:
    print("python json validated")

try:
    user = User.model_validate_json(json_obj)
except ValidationError as err:
    raise err
else:
    print("json validated")

user = User(**js)
print(user.model_dump())

user = User.parse_obj(js)
print(user.model_dump())

user = User.parse_raw(json_obj)
print(user.model_dump())