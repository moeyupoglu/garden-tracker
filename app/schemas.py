from pydantic import BaseModel,EmailStr, conint,Field
from datetime import datetime
from typing import Optional





class UserCreate(BaseModel):
    email: EmailStr
    password: str





    
    
class UserOut(BaseModel):
    id:int
    email: EmailStr
    created_at:datetime
    class Config:
        orm_mode = True
    

class UserLogin(BaseModel):
    email:EmailStr
    password:str
    
    
class PlantUpdate(BaseModel):
    name: str
    type: str
    location: str
    notes: str
    
    
    
    
    
class Token(BaseModel):
    access_token:str
    token_type:str
    
class TokenData(BaseModel):
    id:Optional[str]=None
    
 
