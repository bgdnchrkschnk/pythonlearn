from typing import Optional

from pydantic import BaseModel, EmailStr, PositiveInt, HttpUrl, field_validator, ValidationError


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
    hobbies: Optional[list[Hobbie]]

    @field_validator("sex")
    @classmethod
    def sex_field_validate(cls, value: str) -> str:
        possible_values = {"male", "female"}
        if value not in possible_values:
            raise ValueError(f"Unsupported sex value: Possible: {possible_values}")
        return value


singing_dict = {"name": "Nikita",
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

# print(bogdan.model_dump_json(indent=True))

# try:
#     User.model_validate(bogdan_dict)
# except ValidationError as err:
#     raise err
# else:
#     print(f"object bogdan_dict validated")

print(bogdan.hobbies[0].json())

