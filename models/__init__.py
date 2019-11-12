#!/usr/bin/python3
"""
Provides the 'models' package
"""
import models
from . import engine
from . import base_model
from . import amenity
from . import city
from . import place
from . import state
from . import review
from . import user


def getmodel(name):
    """
    Get a model by name
    """
    for item in dir(models):
        attr = getattr(models, item)
        if type(attr) is type(models) and name in dir(attr):
            match = getattr(attr, name)
            if type(match) is type:
                return (match)
    return None


storage = engine.file_storage.FileStorage()
storage.reload()
