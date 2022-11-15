#!/usr/bin/python3
"""This class will defines all common attributes/methods
    for other  classes"""


import uuid
from datetime import datetime


class BasePerson:

    first_name: str
    surname: str
    birthday: str
    pictur_url: str
    id_card_url: str

    def __init__(self, *args, **kwargs):
        date_format = "%Y-%m-%dT%H:%M:%S.%f"
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key != '__class__':
                    self.__dict__[key] = value
                if key in ("created_at", "updated_at"):
                    self.__dict__[key] = datetime.strptime(value, date_format)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def save(self):
        """ updates the public instance attribute updated_at to current"""
        self.updated_at = datetime.now()

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


if __name__=="__main__":
    my_model = BasePerson()
    my_model.first_name = "remi"
    my_model.surname = "jake"
    my_model.id_card_url = "url"
    my_model.birthday = datetime(1990, 11, 28, 23, 55, 59, 342380)
    print(my_model)
    #my_model.save()
    print(my_model)
    print(type(my_model.created_at))
    print("--")
    my_model_json = my_model.to_dict()
    print(my_model_json)
    print("JSON of my_model:")
    for key in my_model_json.keys():
        print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))
    print("--")
    my_new_model = BasePerson(**my_model_json)
    print(my_new_model.id)
    print(my_new_model)
    print(type(my_new_model.created_at))
    print("--")
    print(my_model is my_new_model)
