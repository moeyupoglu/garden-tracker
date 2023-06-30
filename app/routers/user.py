from pydantic import EmailStr
from sqlalchemy import func
from app import oauth2
from .. import models,schemas,utils
from fastapi import FastAPI, Form, Request,Response,status,HTTPException,Depends,APIRouter
from sqlalchemy.orm import Session
from typing import List, Optional
from ..database import get_db
from fastapi.responses import HTMLResponse



router = APIRouter(
    prefix= "/users",
    tags=['Users']
)




#method to create new user
@router.post("/signup", status_code=status.HTTP_201_CREATED)
async def create_user(request:Request,email:EmailStr= Form(...),password:str= Form(...), db: Session = Depends(get_db) ):
    
    #hash the pw
    hash_pw=utils.hash(password)
    pw=hash_pw
    new_user=models.User(email=email,password=pw)  
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return new_user






