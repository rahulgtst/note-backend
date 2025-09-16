from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional, List

# ---------- User ----------
class UserBase(BaseModel):
    username: str
    email: EmailStr

class UserCreate(UserBase):
    password: str

class UserResponse(UserBase):
    _id: str
    createdOn: datetime

    class Config:
        from_attributes = True


# ---------- Note ----------
class NoteBase(BaseModel):
    title: str
    content: Optional[str] = None

class NoteCreate(NoteBase):
    pass

class NoteUpdate(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None

class NoteResponse(NoteBase):
    _id: str
    createdOn: datetime
    userId: str

    class Config:
        from_attributes = True


# ---------- Auth ----------
class UserLogin(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"

class TokenData(BaseModel):
    user_id: Optional[str] = None
