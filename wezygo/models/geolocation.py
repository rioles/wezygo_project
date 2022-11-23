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
    merchants = relationship("Merchant", backref="Geolocation", cascade="delete")
    truck_owners = relationship("TruckOwner", backref="Geolocation", cascade="delete")
    #truck_owner = relationship("TruckOwner", backref="Geolocation", cascade="delete")

    @property
    def truck_owners(self):
        truck_owners_dict = models.storage.all(models.classes["TruckOwner"])
        truck_owners_list = []

        for key, value in truck_owners_dict.items():
            if value.geocoordinate_id == self.id:
                truck_owners_list.append(value)
        return truck_owners_list
    

    @property
    def merchants(self):
        merchants_dict = models.storage.all(models.classes["Merchant"])
        merchants_list = []

        for key, value in merchants_dict.items():
            if value.geocoordinate_id == self.id:
                merchants_list.append(value)
        return merchants_list
