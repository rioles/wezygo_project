import datetime
from models.base_person import Base
from models.base_person import BasePerson
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import String, DateTime, Float
from sqlalchemy.orm import relationship
import models
from os import environ
class TruckOwner(BasePerson, Base):
    __tablename__ = "truck_owner"
    first_name = Column(String(128), nullable=False)
    surn_name = Column(String(128), nullable=False)
    birthday = Column(DateTime, default=datetime.datetime.utcnow)
    trucks = relationship("Truck", backref="TruckOwner", cascade="delete")
    #geolocation_id = Column(String(60), ForeignKey("geolocation.id"), nullable=True)

    @property
    def trucks(self):
        trucks_dict = models.storage.all(models.classes["Truck"])
        trucks_list = []

        for key, value in trucks_dict.items():
            if value.truck_owner_id == self.id:
                trucks_list.append(value)
        return trucks_list
    