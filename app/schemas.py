from pydantic import BaseModel

class KeyValueCreate(BaseModel):
    key: str
    value: str

class KeyValueResponse(BaseModel):
    key: str
    value: str

    class Config:
        from_attributes = True