import datetime
from models.base_person import Base
from models.base_person import BasePerson
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import String, DateTime, Float
from sqlalchemy.orm import relationship
import models
class Geolocation(BasePerson, Base):

    __tablename__ = "geolocation"
    
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    coordinate_of = Column(String(128), nullable=False)
    merchandises = relationship("Merchandises", backref="Geolocation", cascade="delete")
    trucks = relationship("Truck", backref="Geolocation", cascade="delete")
    #truck_owner = relationship("TruckOwner", backref="Geolocation", cascade="delete")

    @property
    def trucks(self):
        trucks = models.storage.all(models.classes["Truck"])
        truck_list = []

        for key, value in trucks.items():
            if value.geocoordinate_id == self.id:
                truck_list.append(value)
        return truck_list
    

    @property
    def merchants(self):
        merchandises_dict = models.storage.all(models.classes["Marchandises"])
        merchandises_list = []

        for key, value in merchandises_dict.items():
            if value.geocoordinate_id == self.id:
                merchandises_list.append(value)
        return merchandises_list
