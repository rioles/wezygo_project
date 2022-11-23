#!/usr/bin/python3
"""This class will defines all common attributes/methods
    for other  classes"""
import uuid
from datetime import datetime
import models
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import String

Base = declarative_base()

date_format = "%Y-%m-%dT%H:%M:%S.%f"
class BasePerson:
    """Defines the BaseModel class.
    Attributes:
        id (sqlalchemy String): The BaseModel id.
        created_at (sqlalchemy DateTime): The datetime at creation.
        updated_at (sqlalchemy DateTime): The datetime of last update.
    """
    __tablename__ = 'BasePerson'

    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):

        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key != '__class__':
                    self.__dict__[key] = value
                if kwargs.get("created_at", None) and type(self.created_at) is str:
                    self.created_at = datetime.strptime(kwargs["created_at"], date_format)
                else:
                    self.created_at = datetime.utcnow()
                if kwargs.get("updated_at", None) and type(self.updated_at) is str:
                    self.updated_at = datetime.strptime(kwargs["updated_at"], date_format)
                else:
                    self.updated_at = datetime.utcnow()
                #if key in ("created_at", "updated_at") and __dict__[key] != None:
                    #self.__dict__[key] = datetime.strptime(value, date_format)
           
                if kwargs.get("id", None) is None:
                    self.id = str(uuid.uuid4())

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()
            

    def save(self):
        """ updates the public instance attribute updated_at to current"""
        self.updated_at = datetime.utcnow()
        models.storage.new(self)
        models.storage.save()

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def to_dict(self):
        person_dict = {}
        person_dict_without_class_name = self.__dict__
        person_dict["__class__"] = BasePerson.__name__

        for key, value in person_dict_without_class_name.items():
            if key in ("created_at", "updated_at", "birthday"):
                person_dict[key] = value.isoformat()
            else:
                person_dict[key] = value
        return person_dict
    
    def delete(self):
        """delete the current instance from the storage"""
        models.storage.delete(self)