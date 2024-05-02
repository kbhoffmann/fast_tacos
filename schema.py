from pydantic import BaseModel, validator, ValidationError

class Taco(BaseModel):
    protein: str
    tortilla: str = "Corn"
    price: float
    has_guac: bool = True

    @validator('tortilla')
    def validate_tortilla(value):
        value_lower = value.lower()
        if value_lower not in ['corn', 'flour']:
            raise ValueError("Tortilla can either be 'Corn' or 'Flour'")
        return value


    @validator('price')
    def validate_price(cls, price):
        if price < 1.00:
            raise ValueError("You might as well give the taco away! Price must be at least $1.00.")
        elif price >= 10.00:
            raise ValueError("That taco must be plated in gold! Price must be less than 10.00.")
        return price

    class Config:
        orm_mode = True