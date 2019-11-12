#!/usr/bin/python3
"""Provides a class 'FileStorage' to facilitate persistence of models
"""
import json
import models


class FileStorage:
    """Facilitates model persistence via JSON serialization / deserialization
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Get the dictionary of existing model instances
        """
        return self.__class__.__objects

    def new(self, obj):
        """Add a model to the dictionary of existing model instances
        """
        key = '{}.{}'.format(obj.__class__.__name__, obj.id)
        self.__class__.__objects[key] = obj

    def save(self):
        """Save the dictionary of existing model instances to the filesystem
        """
        with open(self.__class__.__file_path, "w") as myFile:
            dictionary = {key: self.__class__.__objects[key].to_dict()
                          for key in self.__class__.__objects}
            json.dump(dictionary, myFile)

    def reload(self):
        """Load the dictionary of saved model instances from the filesystem
        """
        try:
            with open(self.__class__.__file_path, "r") as myFile:
                objects = json.load(myFile)
                for key in objects:
                    cls = models.getmodel(key.split(".")[0])
                    if cls:
                        self.__class__.__objects[key] = cls(**objects[key])
        except FileNotFoundError:
            pass
