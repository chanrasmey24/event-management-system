from pydantic import BaseModel

class UserCreate(BaseModel):
    email: str
    password: str

class UserOut(BaseModel):
    id: int
    email: str
    role: str
    class Config:
        orm_mode = True


class EventBase(BaseModel):
    title: str
    description: str
    date: str
    location: str

class EventOut(EventBase):
    id: int
    creator_id: int
    class Config:
        orm_mode = True


class RegistrationOut(BaseModel):
    id: int
    user_id: int
    event_id: int
    class Config:
        orm_mode = True

class LoginSchema(BaseModel):
    email: str
    password: str
