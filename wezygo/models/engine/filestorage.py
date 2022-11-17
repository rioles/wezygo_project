#!/usr/bin/python3
import json
from datetime import datetime
from models.base_person import BasePerson
import os

class FileStorage:
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        id_base_person = obj.id
        class_name = obj.__class__.__name__
        key_obj = f"{class_name}.{id_base_person}"
        FileStorage.__objects[key_obj] = obj

    def save(self):
        """Serialize __objects to the JSON file __file_path."""
        current_object_dict = FileStorage.__objects
        temp_dict = {}
        for key, value in current_object_dict.items():
            temp_dict[key] = value.to_dict()
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(temp_dict, f)

    def reload(self):
        try:
            with open(FileStorage.__file_path, 'r') as f:
                objdict = json.load(f)
            for key, val in objdict.items():
                name = key.split(".")[0]
                self.new(eval(name)(**val))

        except FileNotFoundError:
            return
        return objdict


        







