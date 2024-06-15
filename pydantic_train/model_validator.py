from typing import Optional

from pydantic import BaseModel, EmailStr, PositiveInt, HttpUrl, model_validator


class User(BaseModel):
    name: str = "unnamed"
    sex: str
    age: PositiveInt
    email: EmailStr | None
    account_link: Optional[HttpUrl]
    married: bool
    hobbies: Optional[list[str]]

    @model_validator(mode="before")
    @classmethod
    def validate_not_existing_fields(cls, data: dict):
        for key in data:
            if key not in cls.model_fields:
                raise ValueError(f"{key} field is not expected in schema!")
        return data


bogdan_dict = {"name": "Bogdan",
               "sex": "male",
               "age": 18,
               "email": "testemail@gmail.com",
               "married": True,
               "account_link": "https://vk.com",
               "hobbies": ["singing"],
               "model": "tesla"}

bogdan = User(**bogdan_dict)

# print(bogdan.model_dump_json(indent=True))
