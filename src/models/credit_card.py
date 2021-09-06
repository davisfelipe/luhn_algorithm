from pydantic import BaseModel, Field, validator


class InputCreditCard(BaseModel):
    number: str = Field(..., min_length=16, max_length=16)

    @validator('number', pre=True)
    def validate_number(cls, value: str):
        new_value = value.replace(" ", "")
        if not new_value.isdigit():
            raise ValueError('must contain only numbers')
        return new_value
