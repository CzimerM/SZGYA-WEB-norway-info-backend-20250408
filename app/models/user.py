from sqlmodel import Field, SQLModel, Relationship
from typing import Optional
from datetime import date

class UserBase(SQLModel):
    username: str = Field(default=None, max_length=64)
    high_score: int
    json_save: str
   
class User(UserBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    password_hash: str = Field(default=None, max_length=256)
   
class UserPublicSmall(UserBase):
    id: Optional[int]

class UserPublic(UserPublicSmall):
    pass

class UserCreate(UserBase):
    password: str

class UserUpdate(UserBase):
    pass