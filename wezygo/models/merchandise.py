#!/usr/bin/python3
"""Defines the City class."""
import datetime
from models.base_person import Base
from models.base_person import BasePerson
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import String, DateTime, Float
from sqlalchemy.orm import relationship
from os import environ
class Merchandises(BasePerson, Base):
    __tablename__ = "merchandises"
    type_merchandise = Column(String(128), nullable=False)
    capacity = Column(Float, nullable=True)

    merchant_id = Column(String(60), ForeignKey("merchants.id"), nullable=False)

