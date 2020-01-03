from sqlalchemy.orm import Session
from sqlalchemy.sql import text
import models, json
from math import acos, sin, cos


# def get_user(db: Session, user_id: int):
#     return db.query(models.User).filter(models.User.id == user_id).first()


def create_city(db: Session, lat: float, lng: float, pincode: str, address: str, city : str):
    
    db_city = models.City(key = pincode, place_name = address, admin_name1 = city, latitude = lat, longitude =lng)
    db.add(db_city)
    db.commit()
    db.refresh(db_city)
    return db_city

def get_city(db: Session, lat: float, lng: float ):
    lat=str(lat)
    lng=str(lng)
    db_city = db.query(models.City).filter(models.City.latitude == lat).filter(models.City.longitude == lng).first()
    return db_city

def get_using_postgres(db: Session, lat: float, lng: float, radius: int ):
    radius = radius
    nearest = f"SELECT *, ((latitude - {lat}) * (latitude - {lat})+ (longitude  - {lng}) * (longitude  - {lng})) AS distance FROM city ORDER BY distance ASC "
    #nearest = f"SELECT * FROM city WHERE earth_box(ll_to_earth({lat},{lng}), 5000) @> ll_to_earth(latitude, longitude);"
    result = db.query(models.City).from_statement(text(nearest)).all()

    as_dic = []
    for e in result:
        as_dict = {
            'key' : e.key,
            'place_name' : e.place_name,
            'admin_name1' : e.admin_name1,
        }
        as_dic.append(as_dict)
    return as_dic


def get_using_self(db: Session, lat: float, lng: float, radius: int ):

    def distance(lat1, lng1, lat2, lng2: float):
        d = acos(sin(lat1)*sin(lat2)+cos(lat1)*cos(lat2)*cos(lng1-lng2))*6371
        return d

    db_city = db.query(models.City).all()
    for e in db_city:
        d = distance(lat1=lat, lng1=lng, lat2=float(e.latitude), lng2=float(e.longitude))
        if d <= 5:
            as_dict = {
                'key' : e.key,
                'place_name' : e.place_name,
                'admin_name1' : e.admin_name1,
                'distance' : d
                }
            as_dic.append(as_dict)
    return as_dic


    







