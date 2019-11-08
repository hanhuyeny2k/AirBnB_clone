#!/usr/bin/python3
"""
"""
import json

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
            my_dict = {k: self.__objects[k].to_dict() for k in self.__objects}
            json.dump(my_dict, myFile)

    def reload(self):
        try:
            with open (self.__file_path, "r") as myFile:
                dictionary = json.load(myFile)
                self.__objects = {k: dictionary[k]
                                  for k in dictionary}
        except FileNotFoundError:
            pass
