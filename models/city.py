#!/usr/bin/python3
"""
Provides a class 'City' that inherits from 'BaseModel'
"""
import models


class City(models.base_model.BaseModel):
    """
    Defines a city model
    """
    state_id = ""
    name = ""
