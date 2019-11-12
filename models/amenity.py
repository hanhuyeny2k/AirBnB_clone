#!/usr/bin/python3
"""
Provides a class 'Amenity' that inherits from 'BaseModel'
"""
import models


class Amenity(models.base_model.BaseModel):
    """
    Defines an amenity model
    """
    name = ""
