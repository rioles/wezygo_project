#!/usr/bin/python3
from os import getenv
from sqlalchemy import create_engine
from models.base_person import BasePerson
from models.base_person import Base
from models.geolocation import Geolocation
from models.merchandise import Merchandises
from models.merchant import Merchant
from models.truck_merchandise import TruckMerchandise
from models.truck import Truck
from models.truck_owner import TruckOwner
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker
classes = {"Merchant": Merchant, "TruckOwner": TruckOwner,
           "Merchandises": Merchandises, "Geolocation": Geolocation, "Truck": Truck, "TruckMerchandise": TruckMerchandise}


class DBStorage:
    """Represents a database storage engine.
     Attributes:
        __engine (sqlalchemy.Engine): The working SQLAlchemy engine.
        __session (sqlalchemy.Session): The working SQLAlchemy session.
    """
    __engine=""
    __session=""

    def __init__(self):
          self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".
                                      format(getenv("WEGO_MYSQL_USER"),
                                             getenv("WEGO_MYSQL_PWD"),
                                             getenv("WEGO_MYSQL_HOST"),
                                             getenv("WEGO_MYSQL_DB")),
                                      pool_pre_ping=True)
          
    def all(self, cls=None):
        all_objects = {}
        if cls is None:
            for clss in classes.values():
                objs = self.__session.query(clss).all()
                for obj in objs:
                    key_c = obj.__class__.__name__ + '.' + obj.id
                    all_objects[key_c] = obj
        else:
            if type(cls) == str and cls in classes:
                cls = eval(cls)
                #print(cls)
            objs = self.__session.query(cls).all()
            for obj in objs:
                key_c = obj.__class__.__name__ + '.' + obj.id
                all_objects[key_c] = obj

        return all_objects
    
    def new(self, obj):
        """Add obj to the current database session."""
        self.__session.add(obj)

    def update(self, obj):
        cls = obj.__class__.name
        self.__session.query(cls).filter_by(id=obj.id).update({column: getattr(obj, column) for column in cls.__table__.columns.keys()})
       
    def update(self, cls, id_object, id_geolocation):
        self.__session.query(cls).filter_by(id=id_object).update({"geolocation_id": id_geolocation})
        self.save()


    def save(self):
        """Commit all changes to the current database session."""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete obj from the current database session."""
        if obj is not None:
            self.__session.delete(obj)
    
    def get(self, cls, id):
        """
        Returns the object based on the class name and its ID, or
        None if not found
        """
        if cls not in classes.values():
            return None

        all_cls = self.all(cls)
        for value in all_cls.values():
            if (value.id == id):
                return value

        return None

    def reload(self):
        """Create all tables in the database and initialize a new session."""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """Close the working SQLAlchemy session."""
        self.__session.close()