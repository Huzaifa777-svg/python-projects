from pydantic import BaseModel

# Request model for user signup/login
class UserCreate(BaseModel):
    username: str
    password: str

# Response model (jo API return kare)
class UserOut(BaseModel):
    id: int
    username: str

    class Config:
        orm_mode = True
