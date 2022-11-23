import datetime

from models.base_person import Base
from models.base_person import BasePerson
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import String, DateTime, Float
from sqlalchemy.orm import relationship
import models
from os import environ
class Merchant(BasePerson, Base):
    __tablename__ = "merchants"
    first_name = Column(String(128), nullable=False)
    surn_name = Column(String(128), nullable=False)
    birthday = Column(DateTime, default=datetime.datetime.utcnow)
    merchandises = relationship("Merchandises", backref="Merchant", cascade="delete")
    geolocation_id = Column(String(60), ForeignKey("geolocation.id"), nullable=False)


    @property
    def merchandise(self):
        merchandises_dict = models.storage.all(models.classes["Merchandises"])
        merchandises_list = []

        for key, value in merchandises_dict.items():
            if value.truck_owner_id == self.id:
                merchandises_list.append(value)
        return merchandises_list
    