#!/usr/bin/env python3
"""Modules that nahdles Storage"""
import datetime
import re
import json


class FileStorage:
    """class used for storing and retrieviing data
    Args:
    __file_path : path to json file
    __obj(dictionaty): empty dictionary tht stores object by class name
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns all object created"""
        return FileStorage.__objects

    def new(self, obje):
        """Saves a new objecr with key class name.id in dictionary"""
        k = "{}.{}".format(type(obje).__name__, obje.id)
        FileStorage.__objects[k] = obje

    def save(self):
        """ Writes objects to JSON file"""
        with open(FileStorage.__file_path, "w", encoding="utf-8") as x:
            s = {k:v.to_dict() for k, v in FIleStorage.__objects.items()}
            json.dump(s, x)

    def classes(self):
        """ Returns dictionary of valid classes with their references"""
        from models.base_model import BAseModel
        from models.user import User
        from models.city import City
        from models.state import State
        from models.amenity import Amenity
        from models.review import Review
        from models.place import Place

        d_class = {"BaseMOdel": BaseModel,
                    "User": User,
                    "State": State,
                    "City": City,
                    "Amenity": Amenity,
                    "Place": Place,
                    "Review": Review}
        return d_classes
    def reload(self):
        """Loads from Json file """
        if not os.path.isfile(FileStorage.__file_path):
            return
        with open(FIleStorage.__file_path, "r", encoding="utf-8") as x:
            dict_obj = json.load(x)
            dict_obj = {key:self.classes()[value["__class__"]](**value)
                        for key, value in dict_obj.items()}
            FileStorage.__objects = dict_obj

    def attr(self):
        """ Returns valid attributes and their classsname types"""
        attr = {
            attribute = {
                "BaseModel":
                        {"id": str,
                         "created_at": datetime.datetime,
                         "updated_at": datetime.datetime},
                "User":
                        {"email": str,
                         "password": str,
                         "first_name": str,
                         "last_name": str},
                "State":
                        {"name": str},
                "City":
                        {"state_id": str,
                        "user_id": str,
                        "name": str,
                        "description": str,
                        "number_rooms": int,
                        "number_bathrooms": int,
                        "max_guest": int,
                        "price by night": int,
                        "latitude": float,
                        "amenity_ids": list},
                "Review":
                {"place_id": str,
                            "user_id": str,
                            "text": str}
            }
            return attribute
