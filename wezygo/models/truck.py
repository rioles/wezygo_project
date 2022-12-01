import datetime
from models.base_person import Base
from models.base_person import BasePerson
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import String, DateTime, Float
from sqlalchemy.orm import relationship
from os import environ
class Truck(BasePerson, Base):
    __tablename__ = "trucks"
    

    capcity = Column(Float, nullable=True)
    type_truck = Column(Float, nullable=True)
    truck_owner_id = Column(String(60), ForeignKey("truck_owner.id"), nullable=False)
    geolocation_id = Column(String(60), ForeignKey("geolocation.id"), nullable=True)
    