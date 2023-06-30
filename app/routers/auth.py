from jose import JWTError
import jwt

from app import main
from .. import models,schemas,utils,oauth2
from fastapi import FastAPI, Path, Request,Response,status,HTTPException,Depends,APIRouter
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from typing import List
from .. import database 
from fastapi.responses import RedirectResponse,HTMLResponse
from fastapi import Response, status
from .. database import engine,get_db




router = APIRouter(tags=['Authentication'])

@router.post("/login/user",response_model=schemas.Token)
def login(response: Response,user_credentials:OAuth2PasswordRequestForm = Depends(),db:Session = Depends(database.get_db)):
    
    #it has two things -- username and password
    user = db.query(models.User).filter(models.User.email==user_credentials.username).first()
    
    if not user:
        raise HTTPException(
            status_code = status.HTTP_403_FORBIDDEN , detail = f"Invalid Credentials!"
            )
    if not utils.verify(user_credentials.password,user.password):
        raise HTTPException(
            status_code = status.HTTP_403_FORBIDDEN , detail = f"Invalid Credentials!"
            )
    
    access_token = oauth2.create_access_token(data = {"user_id":user.id})
    response.set_cookie(key="jwtToken", value=access_token, httponly=True)
    return {"access_token":access_token,"token_type":"bearer"}

  
    













@router.get("/protected")
async def protected_endpoint(user: models.User = Depends(oauth2.get_current_user)):
    headers = {
        "Cache-Control": "no-store, no-cache, must-revalidate",
        "Pragma": "no-cache",
        "Expires": "0",
    }
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,detail=f"Could not validate Credentials!"
            )
    return {"message": "You have accessed the protected endpoint!"}


@router.get("/protecteduser")
async def protected_endpoint_stu(user: models.User = Depends(oauth2.get_current_user)):
    headers = {
        "Cache-Control": "no-store, no-cache, must-revalidate",
        "Pragma": "no-cache",
        "Expires": "0",
    }
    print(user)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,detail=f"Could not validate Credentials!"
            )
    return {"message": "You have accessed the protected endpoint!"}











@router.get("/current-user")
async def get_current_user(user: models.User = Depends(oauth2.get_current_user)):
    return {"email": user.email, "user_id": user.id}













# @router.post("/login")
# def login(user_credentials: schemas.UserLogin,db:Session = Depends(database.get_db)):
#     user = db.query(models.User).filter(models.User.email==user_credentials.email).first()
#     if not user:
#         raise HTTPException(
#             status_code = status.HTTP_404_NOT_FOUND , detail = f"Invalid Credentials!"
#             )
#     if not utils.verify(user_credentials.password,user.password):
#         raise HTTPException(
#             status_code = status.HTTP_404_NOT_FOUND , detail = f"Invalid Credentials!"
#             )
        
#     access_token = oauth2.create_access_token(data = {"user_id":user.id})
#     return {"access_token":access_token,"token_type":"bearer"}