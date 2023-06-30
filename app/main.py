from fastapi import Depends, FastAPI, File, Request, UploadFile
from app import oauth2
from . import models
from . database import engine , get_db
from sqlalchemy.orm import Session
from . routers import plant,user,auth
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles


app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

    



app.include_router(plant.router)
app.include_router(user.router)
app.include_router(auth.router)



@app.get("/login")
async def loginpage(request: Request):
   return templates.TemplateResponse("login.html", {"request": request})


@app.get("/signup")
async def signuppage(request: Request):
   return templates.TemplateResponse("signup.html", {"request": request})

@app.get("/index")
async def indexpage(request: Request):
   return templates.TemplateResponse("index.html", {"request": request})


@app.get("/main")
async def mainhomepage(request: Request):
   return templates.TemplateResponse("main.html", {"request": request})


@app.get("/addplant")
async def addplantpage(request: Request):
   return templates.TemplateResponse("add_plant.html", {"request": request})



@app.get("/viewplant")
async def viewplantpage(request: Request):
   return templates.TemplateResponse("view_plant.html", {"request": request})


@app.get("/editplantmain")
async def editplantmainpage(request: Request):
   return templates.TemplateResponse("edit_plant_main.html", {"request": request})

@app.get("/editplant")
async def editplantpage(request: Request):
   return templates.TemplateResponse("edit_plant.html", {"request": request})



#function to upload image
@app.post("/upload")
def upload(file: UploadFile = File(...),db: Session = Depends(get_db)):
    try:
        contents = file.file.read()
        file_loc=f"static/{file.filename}"
        with open( file_loc, "wb") as f:
            f.write(contents)
        global image_path_save    
        image_path_save=f"{file.filename}"
        
    except Exception:
        return {"message": "There was an error uploading the file"}
    finally:
        file.file.close()
        
    return {"message": f"Successfuly uploaded {file.filename}"}