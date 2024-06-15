from typing import Optional

from pydantic import BaseModel, EmailStr, PositiveInt, HttpUrl


class Hobbie(BaseModel):
    name: str = None
    description: str
    recommendations: list[str] | None


class User(BaseModel):
    name: str = "unnamed"
    sex: str
    age: PositiveInt
    email: EmailStr | None
    account_link: Optional[HttpUrl]
    married: bool
    hobbies: list[Hobbie | None]


singing_dict = {"name":"Nikita",
                "description": "Musician hobbie when person sings",
                "recommendations": ["Regular trainings",
                                    "Drink warm water",
                                    "Sleep well"]
                }


singing = Hobbie(**singing_dict)


bogdan_dict = {"name": "Bogdan",
               "sex": "male",
               "age": 18,
               "email": "testemail@gmail.com",
               "married": True,
               "account_link": "https://vk.com",
               "hobbies": [singing]}

bogdan = User(**bogdan_dict)

print(bogdan.model_dump_json(indent=True))
