#!/usr/bin/python3
"""
"""
import json
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = '{}.{}'.format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        with open(self.__file_path, "w") as myFile:
            dictionary = {key: self.__objects[key].to_dict()
                          for key in self.__objects}
            json.dump(dictionary, myFile)

    def reload(self):
        try:
            with open(self.__file_path, "r") as myFile:
                dictionary = json.load(myFile)
                objs = {}
                for model in dictionary:
                    name = model.split(".")[0]
                    for item in dir(models):
                        attr = getattr(models, item)
                        if type(attr) is type(models) and dir(attr)[0] == name:
                            cls = getattr(attr, dir(attr)[0])
                            objs[model] = cls(**dictionary[model])
                self.__objects = objs
        except FileNotFoundError:
            pass
