from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

import crud, models
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@app.get("/")
async def root():
    return {"message": "Hello, Welcome To City Searching "}


@app.post("/post_location/")
async def create_info(lat: float, lng: float, pincode: str , address: str,city : str, db: Session = Depends(get_db)):
    return crud.create_city(db=db, lat=lat, lng=lng, pincode= pincode, address=address,city= city)

@app.get("/get_location/")
async def create_info(lat: float, lng: float , db: Session = Depends(get_db)):
    return crud.get_city(db=db, lat=lat, lng=lng)

@app.get("/get_using_postgres/")
async def create_info(lat: float, lng: float, radius: int , db: Session = Depends(get_db)):
    return crud.get_using_postgres(db=db, lat=lat, lng=lng, radius=radius)

@app.get("/get_using_self/")
def create_info(lat: float, lng: float, radius: int , db: Session = Depends(get_db)):
    return crud.get_using_self(db=db, lat=lat, lng=lng, radius=radius)