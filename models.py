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

    def __repr__(self):
        """"""
        return "<User - '%s': '%s' - '%s'>" % (self.key, self.place_name,
                                                 self.admin_name1)

















