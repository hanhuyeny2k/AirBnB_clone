#!/usr/bin/python3
"""
"""
import json
from models.base_model import BaseModel

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = '{}.{}'.format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        with open (self.__file_path, "w") as myFile:
            dictionary = {key: self.__objects[key].to_dict()
                          for key in self.__objects}
            json.dump(dictionary, myFile)

    def reload(self):
        try:
            with open (self.__file_path, "r") as myFile:
                dictionary = json.load(myFile)
                self.__objects = {key: BaseModel(**dictionary[key])
                                  for key in dictionary}
        except FileNotFoundError:
            pass
