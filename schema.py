# build a schema using pydantic
from pydantic import BaseModel, field_validator

class Taco(BaseModel):
    protein: str
    tortilla: str = "Corn"
    price: float
    has_guac: bool = True

    @field_validator('tortilla')
    def validate_tortilla(cls, value):
        if value not in ['Corn', 'Flour']:
            raise ValueError("Tortilla can either be 'Corn' or 'Flour'")
        return value

    class Config:
        orm_mode = True