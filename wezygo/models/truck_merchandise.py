import datetime
from models.base_person import Base
from models.base_person import BasePerson
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import String, DateTime, Float
from sqlalchemy.orm import relationship
from os import environ
class TruckMerchandise(BasePerson, Base):
    __tablename__ = "truck_merchandise"
    
    truck_id = Column(String(60), ForeignKey('trucks.id'),nullable=False)
    merchandise_id = Column(String(60), ForeignKey('merchandises.id'),nullable=False)
    prices = Column(Float, nullable=True)
    