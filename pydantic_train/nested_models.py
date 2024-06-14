from typing import Optional

from pydantic import BaseModel


class Hobbie(BaseModel):
    name: str = None
    description: str
    recommendations: list[str] | None


class User(BaseModel):
    name: str = "unnamed"
    sex: str
    age: int
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
               "married": True,
               "hobbies": [singing]}

bogdan = User(**bogdan_dict)

print(bogdan.model_dump_json(indent=True))
