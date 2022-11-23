#!/usr/bin/python3
from os import getenv
from sqlalchemy import create_engine
from models.base_person import BasePerson
from models.base_person import Base
from models.geolocation import Geolocation
from models.merchandise import Merchandises
from models.merchant import Merchant
from models.truck import Truck
from models.truck_owner import TruckOwner
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker
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
        if cls is None:
            objs = self.__session.query(TruckOwner).all()
            objs.extend(self.__session.query(Truck).all())
            objs.extend(self.__session.query(Merchant).all())
            objs.extend(self.__session.query(Merchandises).all())
            objs.extend(self.__session.query(Geolocation).all())
        else:
            if type(cls) == str:
                cls = eval(cls)
            objs = self.__session.query(cls)
        return objs
    
    def new(self, obj):
        """Add obj to the current database session."""
        self.__session.add(obj)

    def save(self):
        """Commit all changes to the current database session."""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete obj from the current database session."""
        if obj is not None:
            self.__session.delete(obj)

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