from typing import Optional, List
from pydantic import BaseModel, field_validator, PositiveFloat, ValidationError



class Item(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    price: PositiveFloat
    tax: Optional[float] = None

    @field_validator("name")
    def name_validation(cls, value: str) -> str:
        if len(value) < 3:
            raise ValueError("Name must be at least 3 chars long.")
        
        return value
    

class PaginationResponse(BaseModel):
    total: int
    skip: int
    limit: int
    data: List[Item]
    next: Optional[str] = None
    previous: Optional[str] = None
