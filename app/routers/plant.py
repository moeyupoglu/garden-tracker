import datetime
from app import main
from .. import models,schemas,oauth2
from fastapi import FastAPI, Form, Query, Request,Response,status,HTTPException,Depends,APIRouter
from sqlalchemy.orm import Session,joinedload
from typing import List
from .. database import engine,get_db
from typing import Optional
from sqlalchemy import func
from fastapi.responses import RedirectResponse,HTMLResponse



router = APIRouter(
    prefix= "/plants",
    tags=['Posts']
)















#function to add plant
@router.post("/addplant", status_code=status.HTTP_201_CREATED)
def add_plant(
    request: Request,
    name: str = Form(...),
    type: str = Form(...),
    location: str = Form(...),
    notes: str = Form(...),
    db: Session = Depends(get_db),
    current_user: models.User = Depends(oauth2.get_current_user)
):
    owner_id = current_user.id
    new_plant = models.Plant(
        name=name,
        type=type,
        location=location,
        notes=notes,
        image_path=main.image_path_save,
        owner_id=owner_id,
    )
    db.add(new_plant)
    db.commit()
    db.refresh(new_plant)
    return new_plant





#function to edit plant
@router.post("/editplant", status_code=status.HTTP_201_CREATED)
def edit_plant(
    plant_id: str = Form(...),
    name: str = Form(...),
    type: str = Form(...),
    location: str = Form(...),
    notes: str = Form(...),
    db: Session = Depends(get_db),
):
    print(plant_id)
    plant = db.query(models.Plant).filter(models.Plant.id == plant_id).first()

    if plant:
        plant.name = name
        plant.type = type
        plant.location = location
        plant.notes = notes
        plant.owner_id = plant.owner_id

        db.commit()
        db.refresh(plant)

        return RedirectResponse(url=main.app.url_path_for("mainhomepage"), status_code=status.HTTP_303_SEE_OTHER)

       
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Plant not found")











@router.get("/tracking")
async def view_all_plants(request: Request,user_id: str = Query(...), db: Session = Depends(get_db)):
    owner_id = user_id
    print(owner_id)
    all_plants = db.query(models.Plant).filter(models.Plant.owner_id == owner_id).all()

    
    return main.templates.TemplateResponse("view_plant.html", {"request": request, "plants": all_plants})


@router.get("/edittracking")
async def all_plants_for_edit(request: Request,owner_id: str = Query(...), db: Session = Depends(get_db)):
    owner_id = owner_id
    print(owner_id)
    all_plants = db.query(models.Plant).filter(models.Plant.owner_id == owner_id).all()

    
    return main.templates.TemplateResponse("edit_plant_main.html", {"request": request, "plants": all_plants})




 #to get plants matched with searched keyword
@router.get("/search")
async def search_results(
    request: Request,
    owner_id: str,
    searched_item: str,
    db: Session = Depends(get_db)
):
    # query the database for plants matching the search term and owner ID
    plants = db.query(models.Plant).filter(
        models.Plant.name.ilike(f"%{searched_item}%"),
        models.Plant.owner_id == owner_id
    ).all()

    # render the search results template with the matching plants
    return main.templates.TemplateResponse("view_plant.html", {"request": request, "plants": plants})


#to fetch all plants
@router.get("/all", response_class=HTMLResponse)
async def all_plants(request: Request, db: Session = Depends(get_db)):
    plants = db.query(models.Plant).all()
    return main.templates.TemplateResponse("view_plant.html", {"request": request, "plants": plants})







# to get details of a plant based on its id
@router.get("/plant/{id}")
async def search_results(request: Request,id:str, db: Session = Depends(get_db)):
    id=int(id)
    print(id)
    
    plant = db.query(models.Plant).filter(models.Plant.id==id).first()
    
    if plant is None:
        # return a 404 response if the plant is not found
        raise HTTPException(status_code=404, detail="Plant not found")

    return main.templates.TemplateResponse("one_item.html", {"request": request, "plant": plant})


# to get details of a plant based on its id
@router.get("/edit/{id}")
async def edit_search(request: Request,id:str, db: Session = Depends(get_db)):

    id=int(id)
    print(id)
    plant = db.query(models.Plant).filter(models.Plant.id==id).first()
    if plant is None:
        # return a 404 response if the plant is not found
        raise HTTPException(status_code=404, detail="Plant not found")

    return main.templates.TemplateResponse("edit_plant.html", {"request": request, "plant": plant})
















