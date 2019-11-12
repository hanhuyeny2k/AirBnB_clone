#!/usr/bin/python3
"""
Provides a class 'BaseModel' to serve as a base class for all other models
"""
import models
from datetime import datetime
from uuid import uuid4


class BaseModel:
    """
    Defines functionality common to all models
    """
    def __init__(self, *args, **kwargs):
        """
        Instantiate a model
        """
        if kwargs == {}:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
        else:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    setattr(self, key,
                            datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
                elif key != "__class__":
                    setattr(self, key, value)

    def __str__(self):
        """
        Convert a model to a string
        """
        return "[{model}] ({ident}) {attrs}".format(
            model=self.__class__.__name__,
            attrs=self.__dict__,
            ident=self.id,
        )

    def save(self):
        """
        Save a model to the filesystem
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Convert a model to a dictionary
        """
        dictionary = self.__dict__.copy()
        dictionary["__class__"] = self.__class__.__name__
        dictionary["updated_at"] = self.updated_at.isoformat()
        dictionary["created_at"] = self.created_at.isoformat()
        return dictionary
