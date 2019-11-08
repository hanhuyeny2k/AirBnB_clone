#!/usr/bin/python3
"""
.....
"""
import uuid
import datetime
from models import storage

class BaseModel:
    """Define BaseModel"""

    def __init__(self, *args, **kwargs):
        if kwargs == {}:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            storage.new(self)
        else:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    setattr(self, key,
                            datetime.datetime.strptime
                            (value, "%Y-%m-%dT%H:%M:%S.%f"))
                elif key == "__class__":
                    continue
                else:
                    setattr(self, key, value)

    def __str__(self):
        return ("[{}] ({}) {}".format
                (self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        self.updated_at = datetime.datetime.now()
        storage.save()

    def to_dict(self):
        dictionary = {"my_number": self.my_number,
                      "name": self.name,
                      "__class__": self.__class__.__name__,
                      "updated_at": self.updated_at.isoformat(),
                      "id": self.id,
                      "created_at": self.created_at.isoformat()}
        return dictionary
