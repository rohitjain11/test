from sqlalchemy import Integer, String, Column
from database import Base

class City(Base):
    __tablename__ = "city"

    id = Column(Integer, primary_key=True, index=True)
    key = Column(String)
    place_name = Column(String)
    admin_name1 = Column(String)
    latitude = Column(Integer)
    longitude = Column(Integer)
    accuracy = Column(Integer)

class Geo(Base):
    __tablename__ = "geo"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    type = Column(String)
    parent = Column(String)
    shape = Column(String)
    latitude = Column(Integer)
    longitude = Column(Integer)
    

















